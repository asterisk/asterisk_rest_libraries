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
        res = get_json_from_file(jsonfile)
        if res is None:
            continue

        for api in res['apis']:
            try:
                for opr in api['operations']:
                    try:
                        uri = "http://%s:%s/stasis%s" \
                            % (HOST, PORT, api['object_path'])
                    except KeyError, err:
                        print "KeyError 1 in %s: %s" % (jsonfile, err)
                        continue

                    try:
                        param_obj = generate_params(opr['parameters'])
                    except:
                        param_obj = {}

                    try:
                        if opr['httpMethod'] == 'GET':
                            resp = requests.get(uri, params=param_obj)
                        elif opr['httpMethod'] == 'POST':
                            resp = requests.post(uri, params=param_obj)
                        elif opr['httpMethod'] == 'DELETE':
                            resp = requests.delete(uri, params=param_obj)
                        elif opr['httpMethod'] == 'PUT':
                            resp = requests.put(uri, params=param_obj)
                    except requests.exceptions.ConnectionError:
                        print "Connection refused"
                        return 1

                    if resp is None:
                        continue

                    print "%s %s %s" \
                        % (opr['responseClass'], opr['httpMethod'], uri)

                    if resp.text:
                        print "\t%s: %s" % (resp.status_code, resp.text)
            except KeyError, err:
                print "KeyError 2 in %s: %s" % (jsonfile, err)
                continue


def get_json_from_file(jsonfile):
    """Open file, read JSON, parse JSON, return dictionary"""
    f = open(PATH + "/" + jsonfile, 'r')
    json_string = f.read()
    f.close()
    try:
        res = json.loads(json_string)
    except err:
        #print err
        pass

    return res


def generate_params(ops):
    """Generate example parameters as required for use in REST API call."""
    res = {}
    for opr in ops:
        if opr['dataType'] == 'string':
            if opr['allowMultiple']:
                res[opr['name']] = ['example', 'string']
            else:
                res[opr['name']] = 'example'
        elif opr['dataType'] == 'number':
            if opr['allowMultiple']:
                res[opr['name']] = [20, 8]
            else:
                res[opr['name']] = 20
        elif opr['dataType'] == 'boolean':
            if opr['allowMultiple']:
                res[opr['name']] = [True, False]
            else:
                res[opr['name']] = True

    return res

if __name__ == "__main__":
    sys.exit(main() or 0)
