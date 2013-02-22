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
    def __init__(self):
        """Initialize the Bridge object."""
        self.id = 1

    def get_id(self):
        """Return the Bridge object's id."""
        return self.id

    def delete(self):
        """Delete the Bridge."""
        is_success = True
        return is_success

    def add_channel(self, channel):
        """Add a Channel to the Bridge."""
        is_success = True
        return is_success

    def remove_channel(self, channel):
        """Remove a Channel from the Bridge."""
        is_success = True
        return is_success

    def record(self):
        """Initiate a new Recording on the Bridge."""
        recording = Recording()
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
