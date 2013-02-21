class Endpoint:
    def __init__(self):
        """Initialize the Endpoint object."""
        self.id = 1


    def get_id(self):
        """Return the Endpoint object's id."""
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
