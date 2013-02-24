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
from recording import Recording


class Channel:
    def __init__(self, api):
        """Initialize the Channel object."""
        self.id = 1
        self._api = api

    def get_id(self):
        """Return the Channel object's id."""
        return self.id

    def delete(self):
        """Delete the Channel."""
        self._api.call('channels', http_method='DELETE', object_id=self.id)
        is_success = True
        return is_success

    def reject(self):
        """Reject the Channel."""
        self._api.call('channels', http_method='POST', api_method='reject', \
            object_id=self.id)
        is_success = True
        return is_success

    def answer(self):
        """Answer the Channel."""
        self._api.call('channels', http_method='POST', api_method='answer', \
            object_id=self.id)
        is_success = True
        return is_success

    def hangup(self):
        """Hang the Channel up."""
        self._api.call('channels', http_method='POST', api_method='hangup', \
            object_id=self.id)
        is_success = True
        return is_success

    def mute(self):
        """Mute the Channel."""
        self._api.call('channels', http_method='POST', api_method='mute', \
            object_id=self.id)
        is_success = True
        return is_success

    def unmute(self):
        """Unmute the Channel."""
        self._api.call('channels', http_method='POST', api_method='unmute', \
            object_id=self.id)
        is_success = True
        return is_success

    def record(self):
        """Initiate a new recording on the Channel."""
        self._api.call('channels', http_method='POST', api_method='record', \
            object_id=self.id)
        recording = Recording(self._api)
        return recording

    def dial(self):
        """Originate a new channel and bridge it to this one."""
        self._api.call('channels', http_method='POST', api_method='dial', \
            object_id=self.id)
        is_success = True
        return is_success

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
