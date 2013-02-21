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

    def add_channel(self):
        """Add a Channel to the Bridge."""
        is_success = True
        return is_success

    def remove_channel(self):
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
