#!/usr/bin/env python

import sys
import os
import glob
import json
import requests
from pprint import pprint


HOST = '192.168.1.124'
PORT = '8088'
PATH = '/home/erin/api_stuff'


def main(argv):
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
                        paramObj = generate_params(op['parameters'])
                    except:
                        paramObj = {}

                    try:
                        if op['httpMethod'] == 'GET':
                            resp = requests.get(uri, params=paramObj)
                        elif op['httpMethod'] == 'POST':
                            resp = requests.post(uri, params=paramObj)
                        elif op['httpMethod'] == 'DELETE':
                            resp = requests.delete(uri, params=paramObj)
                        elif op['httpMethod'] == 'PUT':
                            resp = requests.put(uri, params=paramObj)
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
    f = open(PATH + "/" + jsonfile, 'r')
    jsonString = f.read()
    f.close()
    try:
        res = json.loads(jsonString)
    except Exception, e:
        print e
        pass

    return res


def generate_params(ops):
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
    sys.exit(main(sys.argv) or 0)
