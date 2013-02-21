class Recording:
    def __init__(self):
        """Initialize the Recording object."""
        self.id = 1
        self._is_stopped = False
        self._is_paused = False
        self._is_muted = False

    def get_id(self):
        """Return the Recording object's id."""
        return self.id

    def delete(self):
        """Delete the Recording."""
        is_success = True
        return is_success

    def stop(self):
        """Stop recording."""
        self._is_stopped = True
        is_success = True
        return is_success

    def pause(self):
        """Pause recording."""
        self._is_paused = True
        is_success = True
        return is_success

    def unpause(self):
        """Unpause recording."""
        self._is_paused = False
        is_success = True
        return is_success

    def mute(self):
        """Mute recording."""
        self._is_muted = True
        is_success = True
        return is_success

    def unmute(self):
        """Unmute recording."""
        self._is_muted = False
        is_success = True
        return is_success

    def is_stopped(self):
        """Return True or False according to stopped status."""
        return self._is_stopped

    def is_muted(self):
        """Return True or False according to mute status."""
        return self._is_muted

    def is_paused(self):
        """Return True or False according to paused status."""
        return self._is_paused

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
