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
import json
import re
import requests
from api import APIClass
from utils import *
import codewrap


class Generator():
    """Generate Asterisk REST API from Swagger JSON resources

    """
    def __init__(self):
        """Initiate Generator object"""
        self.classes = []

    def run(self, argv):
        """Make API self.classes

        Parse Swagger JSON files and make python API self.classes.

        Uses:
        copyright_notice.bit
        proper_object_def.proto
        proper_object_method_def.proto

        """
        args = parse_args(argv)
        methods_to_move = ['get', 'gets']
        asterisk_class = None
        self.classes = []

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
        if args['dir'] is None and args['url'] is None:
            print "Usage: ./generate_library --lang=language ", \
                  "[--dir=/path/to/resources/ | ", \
                  "--url=http://localhost:8088/stasis] "
            return 1

        template_copyright = get_file_content(
            '%s/templates/copyright.proto' % (args['lang'])
        )
        template_class_def = get_file_content(
            '%s/templates/class_def.proto' % (args['lang'])
        )
        template_method_def = get_file_content(
            '%s/templates/method_def.proto' % (args['lang'])
        )

        if args['dir']:
            self.get_resources_from_dir(args['dir'])
        elif args['url']:
            self.get_resources_from_url(args['url'])

        if len(self.classes) == 0:
            print "No resources found. Are you using Asterisk 12 or later?"
            return 1

        self.classes = sorted(self.classes, cmp=sort_asterisk_first)

        for class_ in self.classes:
            method_texts = []
            print "Generating class %s" % (class_.class_name)
            class_def = class_.construct_file_contents(template_class_def)

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
                filebit = method.construct_file_contents(template_method_def)
                method_texts.append(filebit)

            file_contents = '\n\n'.join([template_copyright, class_def])
            for text in method_texts:
                file_contents = '\n'.join([file_contents, text])

            wrapped_file_contents = codewrap.wrap(file_contents, 79)
            write_file('%s/lib/%s.py' % (args['lang'], class_.file_name),
                       wrapped_file_contents)

        license_content = get_file_content('LICENSE')
        write_file('%s/lib/LICENSE' % args['lang'], license_content)

    def get_resources_from_url(self, url):
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
                self.classes.append(APIClass(res))

    def get_resources_from_dir(self, path):
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
