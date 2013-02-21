class AsteriskPy:
    def __init__(self):
        pass


    def get_info(self):
        """Return dict of Asterisk system information"""
        return 'fantastic'


    def get_endpoints(self):
        """Return a list of all Endpoints from Asterisk."""
        return result_list


    def get_channels(self):
        """Return a list of all Channels from Asterisk."""
        return result_list


    def get_bridges(self):
        """Return a list of all Bridges from Asterisk"""
        return result_list


    def get_recordings(self):
        """Return a list of all Recordings from Asterisk."""
        return result_list


    def get_endpoint(self, object_id):
        """Return Endpoint specified by object_id."""
        result = Endpoint()
        return result


    def get_channel(self, object_id):
        """Return Channel specified by object_id."""
        result = Channel()
        return result


    def get_bridge(self, object_id):
        """Return Bridge specified by object_id."""
        result = Bridge()
        return result


    def get_recording(self, object_id):
        """Return Recording specified by object_id."""
        result = Recording()
        return result


    def add_event_handler(self, event_name, handler):
        """Add a general event handler for Stasis events.

        For object-specific events, use the object's add_event_handler instead.

        """
        pass


    def remove_event_handler(self, event_name, handler):
        """Add a general event handler for Stasis events.

        For object-specific events, use the object's add_event_handler instead.

        """
        pass

