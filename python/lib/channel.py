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


class Channel:
    """Definition of Channel object."""
    def __init__(self, api):
        """Initialize the Channel object."""
        self.object_id = 1
        self._api = api

    def get_id(self):
        """Return the Channel object's id."""
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

    def originate(self, endpoint_string=None, extension_string=None,
                  context_string=None):
        """Active channels

        Create a new channel (originate)

        """
        params = {}
        if endpoint_string:
            params['endpoint'] = endpoint_string
        if extension_string:
            params['extension'] = extension_string
        if context_string:
            params['context'] = context_string

        self._api.call('/api/channels', http_method='POST',
                       api_method='originate', parameters=params)
        is_success = True
        return is_success

    def delete(self):
        """Active channel

        Delete (i.e. hangup) a channel

        """
        params = {}

        self._api.call('/api/channels/%s', http_method='DELETE',
                       api_method='delete', parameters=params,
                       object_id=self.object_id)
        is_success = True
        return is_success

    def dial(self, endpoint_string=None, extension_string=None,
             context_string=None):
        """Create a new channel (originate) and bridge to this channel

        Create a new channel (originate) and bridge to this channel

        """
        params = {}
        if endpoint_string:
            params['endpoint'] = endpoint_string
        if extension_string:
            params['extension'] = extension_string
        if context_string:
            params['context'] = context_string

        self._api.call('/api/channels/%s/dial', http_method='POST',
                       api_method='dial', parameters=params,
                       object_id=self.object_id)
        is_success = True
        return is_success

    def continue_in_dialplan(self):
        """Exit application; continue execution in the dialplan

        Exit application; continue execution in the dialplan

        """
        params = {}

        self._api.call('/api/channels/%s/continue', http_method='POST',
                       api_method='continue_in_dialplan', parameters=params,
                       object_id=self.object_id)
        is_success = True
        return is_success

    def reject(self):
        """Reject a channel

        Reject a channel

        """
        params = {}

        self._api.call('/api/channels/%s/reject', http_method='POST',
                       api_method='reject', parameters=params,
                       object_id=self.object_id)
        is_success = True
        return is_success

    def answer(self):
        """Answer a channel

        Answer a channel

        """
        params = {}

        self._api.call('/api/channels/%s/answer', http_method='POST',
                       api_method='answer', parameters=params,
                       object_id=self.object_id)
        is_success = True
        return is_success

    def mute(self, direction_string='both'):
        """Mute a channel

        Mute a channel

        """
        params = {}
        if direction_string:
            params['direction'] = direction_string

        self._api.call('/api/channels/%s/mute', http_method='POST',
                       api_method='mute', parameters=params,
                       object_id=self.object_id)
        is_success = True
        return is_success

    def unmute(self, direction_string='both'):
        """Unmute a channel

        Unmute a channel

        """
        params = {}
        if direction_string:
            params['direction'] = direction_string

        self._api.call('/api/channels/%s/unmute', http_method='POST',
                       api_method='unmute', parameters=params,
                       object_id=self.object_id)
        is_success = True
        return is_success

    def record(self, name_string=None, max_duration_seconds_number='0',
               max_silence_seconds_number='0', append_boolean='False',
               beep_boolean='False', terminate_on_string='none'):
        """Record audio to/from a channel

        Start a recording

        """
        params = {}
        if name_string:
            params['name'] = name_string
        if max_duration_seconds_number:
            params['maxDurationSeconds'] = max_duration_seconds_number
        if max_silence_seconds_number:
            params['maxSilenceSeconds'] = max_silence_seconds_number
        if append_boolean:
            params['append'] = append_boolean
        if beep_boolean:
            params['beep'] = beep_boolean
        if terminate_on_string:
            params['terminateOn'] = terminate_on_string

        self._api.call('/api/channels/%s/record', http_method='POST',
                       api_method='record', parameters=params,
                       object_id=self.object_id)
        is_success = True
        return is_success
