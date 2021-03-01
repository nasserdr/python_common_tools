#!/usr/bin/python3
"""
Python script that fetches https://intranet.hbtn.io/status
"""

from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("    - type: {}".format(type(html)))
        print("    - Content: {}".format(html))
        print("    - utf8 content: {}".format(html.decode('utf-8')))
