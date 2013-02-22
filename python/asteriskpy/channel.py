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
    def __init__(self):
        """Initialize the Channel object."""
        self.id = 1

    def get_id(self):
        """Return the Channel object's id."""
        return self.id

    def delete(self):
        """Delete the Channel."""
        is_success = True
        return is_success

    def reject(self):
        """Reject the Channel."""
        is_success = True
        return is_success

    def answer(self):
        """Answer the Channel."""
        is_success = True
        return is_success

    def hangup(self):
        """Hang the Channel up."""
        is_success = True
        return is_success

    def mute(self):
        """Mute the Channel."""
        is_success = True
        return is_success

    def unmute(self):
        """Unmute the Channel."""
        is_success = True
        return is_success

    def record(self):
        """Initiate a new recording on the Channel."""
        recording = Recording()
        return recording

    def dial(self):
        """Dial."""
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
