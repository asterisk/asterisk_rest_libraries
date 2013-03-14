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


class Recording:
    """Definition of Recording object."""
    def __init__(self, api):
        """Initialize the Recording object."""
        self.object_id = 1
        self._api = api

    def get_id(self):
        """Return the Recording object's id."""
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

    def delete(self):
        """Individual recording; Delete recording"""
        params = {}

        self._api.call('/api/recordings/%s', http_method='DELETE',
                       parameters=params, object_id=self.object_id)
        is_success = True
        return is_success

    def stop(self):
        """Stop recording"""
        params = {}

        self._api.call('/api/recordings/%s/stop', http_method='POST',
                       parameters=params, object_id=self.object_id)
        is_success = True
        return is_success

    def pause(self):
        """Pause recording"""
        params = {}

        self._api.call('/api/recordings/%s/pause', http_method='POST',
                       parameters=params, object_id=self.object_id)
        is_success = True
        return is_success

    def unpause(self):
        """Unpause recording"""
        params = {}

        self._api.call('/api/recordings/%s/unpause', http_method='POST',
                       parameters=params, object_id=self.object_id)
        is_success = True
        return is_success

    def mute(self):
        """Mute recording"""
        params = {}

        self._api.call('/api/recordings/%s/mute', http_method='POST',
                       parameters=params, object_id=self.object_id)
        is_success = True
        return is_success

    def unmute(self):
        """Unmute recording"""
        params = {}

        self._api.call('/api/recordings/%s/unmute', http_method='POST',
                       parameters=params, object_id=self.object_id)
        is_success = True
        return is_success
