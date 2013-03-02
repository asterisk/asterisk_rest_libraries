#!/usr/bin/env python
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

import sys
import os
import glob
import json
import requests


HOST = '192.168.1.124'
PORT = '8088'
PATH = '/home/erin/asterisk_rest_libraries'


def main():
    """Test Asterisk REST API with HTTP requests derived from Swagger
    JSON Resources.  This does not use generated code or any piece of
    the library package.

    """
    os.chdir(PATH)
    for jsonfile in glob.glob("*.json"):
        res = get_JSON_from_file(jsonfile)
        if res is None:
            continue

        for api in res['apis']:
            try:
                for op in api['operations']:
                    try:
                        uri = "http://%s:%s/stasis%s" \
                            % (HOST, PORT, api['path'])
                    except KeyError, e:
                        print "KeyError 1 in %s: %s" % (jsonfile, e)
                        continue

                    try:
                        param_obj = generate_params(op['parameters'])
                    except:
                        param_obj = {}

                    try:
                        if op['httpMethod'] == 'GET':
                            resp = requests.get(uri, params=param_obj)
                        elif op['httpMethod'] == 'POST':
                            resp = requests.post(uri, params=param_obj)
                        elif op['httpMethod'] == 'DELETE':
                            resp = requests.delete(uri, params=param_obj)
                        elif op['httpMethod'] == 'PUT':
                            resp = requests.put(uri, params=param_obj)
                    except requests.exceptions.ConnectionError:
                        print "Connection refused"
                        return 1

                    if resp is None:
                        continue

                    print "%s %s %s" \
                        % (op['responseClass'], op['httpMethod'], uri)

                    if resp.text:
                        print "\t%s: %s" % (resp.status_code, resp.text)
            except KeyError, e:
                print "KeyError 2 in %s: %s" % (jsonfile, e)
                continue


def get_JSON_from_file(jsonfile):
    """Open file, read JSON, parse JSON, return dictionary"""
    f = open(PATH + "/" + jsonfile, 'r')
    json_string = f.read()
    f.close()
    try:
        res = json.loads(json_string)
    except e:
        #print e
        pass

    return res


def generate_params(ops):
    """Generate example parameters as required for use in REST API call."""
    res = {}
    for op in ops:
        if op['dataType'] == 'string':
            if op['allowMultiple']:
                res[op['name']] = ['example', 'string']
            else:
                res[op['name']] = 'example'
        elif op['dataType'] == 'number':
            if op['allowMultiple']:
                res[op['name']] = [20, 8]
            else:
                res[op['name']] = 20
        elif op['dataType'] == 'boolean':
            if op['allowMultiple']:
                res[op['name']] = [True, False]
            else:
                res[op['name']] = True

    return res

if __name__ == "__main__":
    sys.exit(main() or 0)
