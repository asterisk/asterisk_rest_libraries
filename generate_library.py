#!/usr/bin/env python
"""
Copyright (C) 2013 Digium, Inc.

Erin Spiceland <espiceland@digium.com>

See http://www.asterisk.org for more information about
the Asterisk project. Please do not directly contact
any of the maintainers of this project for assistance;
the project provides a web site, mailing lists and IRC
channels for your use.

 This program is free software, distributed under the terms
 detailed in the the LICENSE file at the top of the source tree.

"""

import sys
sys.path.append("lib")
import json
import re
import requests
from api import APIClass
from utils import parse_args, write_file, get_file_content
import codewrap


class Generator():
    """Generate Asterisk REST API from Swagger JSON resources

    """
    def __init__(self):
        """Initiate Generator object"""
        self.classes = []

    def run(self, argv):
        """Make API self.classes

        Parse Swagger JSON files and make API classes.

        Uses:
        copyright_notice.bit
        proper_object_def.proto
        proper_object_method_def.proto

        """
        args = parse_args(argv)
        methods_to_move = ['get', 'gets']
        asterisk_class = None
        if ((args['dir'] is None or args['dir'] == '')
                and (args['url'] is None or args['url'] == '')) \
                or args['lang'] is None or args['lang'] == '':
            print "Usage: ./generate_library --lang=language ", \
                  "[--dir=/path/to/resources/ | ", \
                  "--url=http://localhost:8088/stasis] "
            return 1

        config = json.loads(get_file_content("%s/config.json" %
                                             (args['lang'])))

        def remove_moved(method):
            """Remove get* methods from this class and add to Asterisk"""
            if method.method_name in methods_to_move:
                # Add these to the Asterisk class instead
                asterisk_class.methods.append(method)
                return False
            else:
                return True

        for class_ in self.classes:
            if class_.class_name == "Asterisk":
                asterisk_class = class_
            class_.methods[:] = [m for m in class_.methods if remove_moved(m)]

        template_copyright = get_file_content(
            '%s/templates/copyright.proto' % (args['lang'])
        ) + '\n'

        if args['dir']:
            self.get_resources_from_dir(args['dir'], args['lang'])
        elif args['url']:
            self.get_resources_from_url(args['url'], args['lang'])

        if len(self.classes) == 0:
            print "No resources found. Are you using Asterisk 12 or later?"
            return 1

        self.classes = sorted(self.classes, cmp=sort_asterisk_first)

        for class_ in self.classes:
            method_texts = []
            print "Generating class %s" % (class_.class_name)
            class_def = class_.construct_file_contents()

            for method in class_.methods:
                if method.method_name in methods_to_move:
                    if class_.class_name != 'Asterisk':
                        continue
                    else:
                        # Rename from get/gets to get_channel, get_channels
                        method.method_name = re.sub('(s*)$', r'_%s\1'
                                                    % (method.file_name),
                                                    method.method_name)
                        method.file_name = 'asterisk'

                print "  method %s.%s" \
                    % (class_.class_name, method.method_name)
                filebit = method.construct_file_contents()
                method_texts.append(filebit)

            methods_blob = '\n\n'.join(method_texts)
            if methods_blob != '':
                # Handle different number of newlines if we have no methods
                # to add.
                methods_blob = '\n' + methods_blob

            class_def = re.sub('\{CLASS_METHODS\}', methods_blob, class_def)
            file_contents = '\n\n'.join([template_copyright, class_def])
            file_contents = codewrap.wrap(file_contents, 79)
            write_file('%s/lib/%s.%s' % (args['lang'], class_.file_name,
                       config['file_extension']), file_contents)

        license_content = get_file_content('LICENSE')
        write_file('%s/lib/LICENSE' % args['lang'], license_content)

    def get_resources_from_url(self, url, lang):
        """Get JSON Swagger resources from Asterisk and
        appends APIClass created from them to self.classes

        """
        response = requests.get("%s/resources.json" % (url))
        if response.status_code != 200:
            return

        resources_list = json.loads(response.text)
        for each_res in resources_list['apis']:
            each_res['path'] = re.sub('\{format\}', 'json', each_res['path'])
            response = requests.get("%s%s" % (url, each_res['path']))
            if response.status_code != 200:
                continue

            # Allow invalid JSON exception to be raised
            res = json.loads(response.text)

            if res is not None:
                res['lang'] = lang
                self.classes.append(APIClass(res))

    def get_resources_from_dir(self, path, lang):
        """Get JSON Swagger resources from files and
        appends APIClass created from them to self.classes

        """
        resources_json = get_file_content("%s/resources.json" % (path))
        resources_list = json.loads(resources_json)
        for each_res in resources_list['apis']:
            print each_res
            each_res['path'] = re.sub('\{format\}', 'json', each_res['path'])
            json_string = get_file_content("%s%s" %
                                           (path, each_res['path']))
            # Allow invalid JSON exception to be raised
            res = json.loads(json_string)

            if res is not None:
                res['lang'] = lang
                self.classes.append(APIClass(res))


def sort_asterisk_first(x, y):
    """Sort list of resources so that Asterisk is listed first.
    With Asterisk listed first, we can add get* methods to it
    inside the loop instead of having to loop twice.

    """
    if x.class_name == 'Asterisk':
        return -1
    else:
        return 1


if __name__ == "__main__":
    GEN = Generator()
    RES = GEN.run(sys.argv)
    sys.exit(RES or 0)
