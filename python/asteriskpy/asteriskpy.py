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
import requests
import json
from endpoint import Endpoint
from channel import Channel
from bridge import Bridge
from recording import Recording


class AsteriskPy:
    def __init__(self, host='localhost', port='8088', https=False):
        """Initiate new AsteriskPy instance.

        Takes optional string host, string port, boolean https.
        Raise requests.exceptions

        """
        self._host = host
        self._port = port
        if https is False:
            self._protocol = 'http'
        else:
            self._protocol = 'https'

        self._stasis_base = "%s://%s:%s/stasis" \
            % (self._protocol, self._host, self._port)

        try:
            requests.get("%s/asterisk.json" % (self._stasis_base))
        except requests.exceptions.ConnectionError:
            raise AsteriskPyAccessException(
                "Cannot access URI %s" % (self._stasis_base)
            )

    def get_info(self):
        """Return dict of Asterisk system information"""
        return 'fantastic'

    def get_endpoints(self):
        """Return a list of all Endpoints from Asterisk."""
        result_list = [Endpoint(), Endpoint()]
        return result_list

    def get_channels(self):
        """Return a list of all Channels from Asterisk."""
        result_list = [Channel(), Channel()]
        return result_list

    def get_bridges(self):
        """Return a list of all Bridges from Asterisk"""
        result_list = [Bridge(), Bridge()]
        return result_list

    def get_recordings(self):
        """Return a list of all Recordings from Asterisk."""
        result_list = [Recording(), Recording()]
        return result_list

    def get_endpoint(self, object_id):
        """Return Endpoint specified by object_id."""
        result = Endpoint()
        return result

    def get_channel(self, object_id):
        """Return Channel specified by object_id."""
        result = Channel()
        return result

    def get_bridge(self, object_id):
        """Return Bridge specified by object_id."""
        result = Bridge()
        return result

    def get_recording(self, object_id):
        """Return Recording specified by object_id."""
        result = Recording()
        return result

    def add_event_handler(self, event_name, handler):
        """Add a general event handler for Stasis events.
        For object-specific events, use the object's add_event_handler instead.
        """
        pass

    def remove_event_handler(self, event_name, handler):
        """Add a general event handler for Stasis events.
        For object-specific events, use the object's add_event_handler instead.
        """
        pass

    class AsteriskPyAccessException(Exception):
        def __init__(self, m):
            self.message = m

        def __str__(self):
            return self.message

        def _call_api_method(self, uri, params):
            pass
