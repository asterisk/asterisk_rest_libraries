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

class Asterisk:
    def __init__(self, api):
        """Initialize the Asterisk object."""
        self.id = 1
        self._api = api

    def get_id(self):
        """Return the Asterisk object's id."""
        return self.id

    def add_event_handler(self, event_name, handler):
        """Add an event handler for Stasis events on this object.
        For general events, use Asterisk.add_event_handler instead.
        """
        pass

    def remove_event_handler(self, event_name, handler):
        """Remove an event handler for Stasis events on this object.
        For general events, use Asterisk.remove_event_handler instead.
        """
        pass

    def get_info(self, only_string_list=None):
        """Asterisk system information (similar to core show settings)

        Gets Asterisk system information

        """
        params = {}
        if only_string_list:
            params['only'] = only_string_list

        self._api.call('/api/asterisk/info', http_method='GET',
                       api_method='get_info', parameters=params)
        is_success = True
        return is_success

    def get_endpoints(self, withType_string_list=None):
        """Asterisk endpoints

        List available endoints

        """
        params = {}
        if withType_string_list:
            params['withType'] = withType_string_list

        self._api.call('/api/endpoints', http_method='GET',
                       api_method='get_endpoints', parameters=params)
        is_success = True
        return is_success

    def get_endpoint(self):
        """Single endpoint

        Details for an endpoint

        """
        params = {}

        self._api.call('/api/endpoints/%s', http_method='GET',
                       api_method='get_endpoint', parameters=params,
                       object_id=self.id)
        is_success = True
        return is_success

    def get_channels(self):
        """Active channels

        List active channels

        """
        params = {}

        self._api.call('/api/channels', http_method='GET',
                       api_method='get_channels', parameters=params)
        is_success = True
        return is_success

    def get_channel(self):
        """Active channel

        Channel details

        """
        params = {}

        self._api.call('/api/channels/%s', http_method='GET',
                       api_method='get_channel', parameters=params,
                       object_id=self.id)
        is_success = True
        return is_success

    def get_bridges(self):
        """Active bridges

        List active bridges

        """
        params = {}

        self._api.call('/api/bridges', http_method='GET',
                       api_method='get_bridges', parameters=params)
        is_success = True
        return is_success

    def get_bridge(self):
        """Individual bridge

        Get bridge details

        """
        params = {}

        self._api.call('/api/bridges/%s', http_method='GET',
                       api_method='get_bridge', parameters=params,
                       object_id=self.id)
        is_success = True
        return is_success

    def get_recordings(self):
        """Recordings

        List recordings

        """
        params = {}

        self._api.call('/api/recordings', http_method='GET',
                       api_method='get_recordings', parameters=params)
        is_success = True
        return is_success

    def get_recording(self):
        """Individual recording

        Get recording details

        """
        params = {}

        self._api.call('/api/recordings/%s', http_method='GET',
                       api_method='get_recording', parameters=params,
                       object_id=self.id)
        is_success = True
        return is_success
