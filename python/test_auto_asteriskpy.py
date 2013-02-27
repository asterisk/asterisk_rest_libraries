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
import auto_asteriskpy


HOST = '10.24.67.73'
#HOST = '192.168.1.124'
PORT = '8088'


def main(argv):
    ast = auto_asteriskpy.AsteriskPy(host=HOST, port=PORT)
    result = ast.get_info()
    print "Asterisk status is %s" % (result)

    endpoints = ast.get_endpoints()
    channels = ast.get_channels()
    bridges = ast.get_bridges()
    recordings = ast.get_recordings()
    channel = ast.create_channel({'tech' : 'dummy_params'})
    bridge = ast.create_bridge({'tech' : 'dummy_params'})

    for endpoint in endpoints:
        print "got endpoint with id %s" % (endpoint.get_id())

    for channel in channels:
        print "got channel with id %s" % (channel.get_id())
        print "method delete returns %s" % (channel.delete())
        print "method reject returns %s" % (channel.reject())
        print "method answer returns %s" % (channel.answer())
        print "method mute returns %s" % (channel.mute())
        print "method unmute returns %s" % (channel.unmute())
        print "method record returns %s" % (channel.record('rec name'))
        print "method dial returns %s" % (channel.dial())

    chan = auto_asteriskpy.Channel(ast._api)
    for bridge in bridges:
        print "got bridge with id %s" % (bridge.get_id())
        print "method delete returns %s" % (bridge.delete())
        print "method add_channel_to returns %s" \
            % (bridge.add_channel_to(chan.get_id()))
        print "method remove_channel_from returns %s" \
            % (bridge.remove_channel_from(chan.get_id()))
        print "method record returns %s" % (bridge.record('rec name'))

    for recording in recordings:
        print "got recording with id %s" % (recording.get_id())
        print "method delete returns %s" % (recording.delete())
        print "method stop returns %s" % (recording.stop())
        print "method pause returns %s" % (recording.pause())
        print "method unpause returns %s" % (recording.unpause())
        print "method mute returns %s" % (recording.mute())
        print "method unmute returns %s" % (recording.unmute())

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv) or 0)
