#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

import urllib.request

req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
   the_page = response.read()
   print("Body response:")
   print("\t- type: {}".format(req.encoding))


 #Body response:$
#    - type: <class 'bytes'>$
#    - content: b'OK'$
#    - utf8 content: OK$
