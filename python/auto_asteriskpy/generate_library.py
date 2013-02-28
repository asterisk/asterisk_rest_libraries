#!/usr/bin/env python
"""
 Copyright (C) 2013 Digium, Inc.

 Erin Spiceland <espiceland@digium.com>

 See http://www.asterisk.org for more information about
 the Asterisk project. Please do not directly contact
 any of the maintainers of this project for assistance;
 the project provides a web site, mailing lists and IRC
 channels for your use.

 This program is free software, distributed under the terms of
 the GNU General Public License Version 2. See the LICENSE file
 at the top of the source tree.

"""

import sys
import os
import glob
import json
import requests
from api import APIClass
import codewrap
from pprint import pprint


HOST = '10.24.67.73'
#HOST = '192.168.1.124'
PORT = '8088'
PATH = '/home/erin/asterisk_rest_libraries'


def main(argv):
    """Make API classes

    Parse Swagger JSON files and make python API classes.

    Uses:
    copyright_notice.bit
    proper_object_def.proto
    proper_object_method_def.proto

    """
    classes = []
    stasis_base = "http://%s:%s/stasis" % (HOST, PORT)
    template_copyright = get_file_content('templates/copyright_notice.bit')
    template_class_def = get_file_content('templates/class_def.proto')
    template_method_def = get_file_content('templates/method_def.proto')

    for jsonfile in glob.glob("%s/*.json" % (PATH)):
        if jsonfile == "%s/resources.json" % (PATH):
            continue
        res = get_object_from_JSON_file(jsonfile)
        if res is None:
            continue

        classes.append(APIClass(res))

    for class_ in classes:
        class_def = class_.construct_file_contents(template_class_def,
                                                   template_method_def)
        method_texts = []
        for method in class_.methods:
            if method.method_name in ['get', 'gets']:
                continue
            filebit = method.construct_file_contents(template_method_def)
            method_texts.append(filebit)

        file_contents = '\n'.join([template_copyright, class_def])
        for text in method_texts:
            file_contents = '\n'.join([file_contents, text])

        wrapped_file_contents = codewrap.wrap(file_contents, 79)
        write_file('%s.py' % (class_.file_name), wrapped_file_contents)

def get_object_from_JSON_file(jsonfile):
    jsonString = get_file_content(jsonfile)
    try:
        res = json.loads(jsonString)
    except Exception, e:
        print e
        pass

    return res

def get_file_content(filepath):
    f = open(filepath, 'r')
    file_content = f.read()
    f.close()
    return file_content

def write_file(filepath, contents):
    f = open(filepath, 'w')
    f.write(contents)
    f.close()

if __name__ == "__main__":
    sys.exit(main(sys.argv) or 0)
