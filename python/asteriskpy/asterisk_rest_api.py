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
import requests
import json
from error import *


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
             parameters=None, object_id=None,
             on_success=None, on_error=None):
        request_uri = "%s/%s" % (self._base_uri, object_path)
        if object_id is not None:
            request_uri = request_uri + "/%s" % (object_id)

        if api_method is not None:
            request_uri = request_uri + "/%s" % (api_method)

        print "request_uri is %s" % (request_uri)

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
            return True

        if resp.text is not None:
            try:
                response_object = json.dumps(resp.text)
            except:
                if on_error is not None:
                    on_error(uri=request_uri, error="Invalid JSON")

            if on_success is not None:
                on_success(uri=request_uri, result=response_object)
            else:
                return True
        else:
            if on_success is not None:
                on_success(uri=request_uri)
            else:
                return True

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
