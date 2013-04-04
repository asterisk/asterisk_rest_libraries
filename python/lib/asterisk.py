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
    """Definition of Asterisk object."""
    def __init__(self, api):
        """Initialize the Asterisk object."""
        self.object_id = 1
        self._api = api

    def get_id(self):
        """Return the Asterisk object's id."""
        return self.object_id

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
        """Asterisk system information (similar to core show settings); Gets
         Asterisk system information"""
        params = {}
        if only_string_list:
            params['only'] = only_string_list

        self._api.call('/asterisk/info', http_method='GET', parameters=params)
        is_success = True
        return is_success
