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
from asteriskpy import AsteriskPy, Endpoint, Channel, Bridge, Recording


HOST = '192.168.1.124'
PORT = '8088'


def main(argv):
    ast = AsteriskPy(host=HOST, port=PORT)
    result = ast.get_info()
    print "Asterisk status is %s" % (result)

    endpoint = Endpoint()
    channel = Channel()
    bridge = Bridge()
    recording = Recording()

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv) or 0)
