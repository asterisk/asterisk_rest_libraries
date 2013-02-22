#!/usr/bin/env python

import sys
from asteriskpy import AsteriskPy, Endpoint, Channel, Bridge, Recording


HOST = '192.168.1.124'
PORT = '8088'


def main(argv):
   ast = AsteriskPy(host=HOST, port=PORT)
   result = ast.get_info()
   print "Asterisk status is %s" % (result)

   endpoint = Endpoint()
   channel = Channel()
   bridge = Bridge()
   recording = Recording()

   return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv) or 0)
