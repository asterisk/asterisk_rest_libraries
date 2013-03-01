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
import requests
import json
import re
from errors import *


class AsteriskRestAPI:
    def __init__(self, uri='localhost'):
        """Initiate new AsteriskRestAPI instance.

        Takes REST API URI. Default http://localhost:8088/stasis/api
        from AsteriskPy._stasis_base

        """
        self._base_uri = uri

        try:
            requests.get("%s/asterisk.json" % (self._base_uri))
        except requests.exceptions.ConnectionError:
            raise AsteriskPyAccessException(
                "Cannot access URI %s" % (self._base_uri)
            )

    def call(self, object_path,
             http_method='GET', api_method=None,
             parameters=None, object_id=None):
        """Call an Asterisk API method, return result dictionary

        Throws AsteriskPyAccessException if the server is unreachable.
        Returns a dict of the following structure:

        {
            'success' : True, # or False
            'response' : jsonObject, # or None
            'error' : None, # or string
        }

        success indicates the success or failure of the Asterisk API call.
        response is a dictionary constructed by json.dumps(json_string)
        error is a message.

        If the API call is successful but Asterisk returns invalid JSON, error
        will be "Invalid JSON." and response will be the unchanged content
        of the response.

        """
        result = {'success' : False, 'response' : None, 'error' : None}
        if object_id:
            object_path = object_path % (object_id)

        request_uri = "%s/%s" % (self._base_uri, object_path)
        if object_id is not None:
            request_uri = request_uri + "/%s" % (object_id)

        if api_method is not None:
            request_uri = request_uri + "/%s" % (api_method)

        try:
            if http_method == 'GET':
                resp = requests.get(request_uri, params=parameters)
            elif http_method == 'POST':
                resp = requests.post(request_uri, params=parameters)
            elif http_method == 'DELETE':
                resp = requests.delete(request_uri, params=parameters)
            elif http_method == 'PUT':
                resp = requests.put(request_uri, params=parameters)
        except requests.exceptions.ConnectionError:
            raise self.AsteriskPyAccessException(
                "Cannot access URI %s" % (request_uri)
            )

        if resp is None:
            # No response or exception? This will probably never happen.
            result['error'] = "No response."
            return result

        if resp.status_code in [418, 200]:
            result['success'] = True
        else:
            result['error'] = "HTTP error occurred: %s" % (resp.status_code)
            return result

        try:
            result['response'] = json.loads(resp.text)
        except ValueError:
            result['response'] = resp.text
            result['error'] = "Invalid JSON."

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

    class AsteriskPyAccessException(Exception):
        def __init__(self, m):
            self.message = m

        def __str__(self):
            return self.message
