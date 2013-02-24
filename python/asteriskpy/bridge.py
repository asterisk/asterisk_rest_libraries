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
from channel import Channel
from recording import Recording


class Bridge:
    def __init__(self, api):
        """Initialize the Bridge object."""
        self.id = 1
        self._api = api;

    def get_id(self):
        """Return the Bridge object's id."""
        return self.id

    def delete(self):
        """Delete the Bridge."""
        self._api.call('bridges', http_method='DELETE', object_id=self.id)
        is_success = True
        return is_success

    def add_channel(self, channel):
        """Add a Channel to the Bridge."""
        params = {'channel' : channel}
        self._api.call('add-channel', http_method='POST', object_id=self.id, \
            parameters={'channel-id' : channel.get_id()})
        is_success = True
        return is_success

    def remove_channel(self, channel):
        """Remove a Channel from the Bridge."""
        params = {'channel' : channel}
        self._api.call('remove-channel', http_method='POST', \
            object_id=self.id, parameters={'channel-id' : channel.get_id()})
        is_success = True
        return is_success

    def record(self):
        """Initiate a new Recording on the Bridge."""
        self._api.call('record', http_method='POST', object_id=self.id)
        recording = Recording(self._api)
        return recording

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
