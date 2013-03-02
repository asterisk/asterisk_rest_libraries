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


def get_file_content(filepath):
    f = open(filepath, 'r')
    file_content = f.read()
    f.close()
    return file_content


def write_file(filepath, contents):
    f = open(filepath, 'w')
    f.write(contents)
    f.close()


def parse_args(argv):
    argv.pop(0)
    args = {
            'dir' : None,
            'url' : None,
            'lang' : 'python',
    }
    for a in argv:
        pieces = a.split("=", 1)
        try:
            args[pieces[0].strip('-')] = pieces[1]
        except:
            args[pieces[0].strip('-')] = True

    return args
