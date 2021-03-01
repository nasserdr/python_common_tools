#!/usr/bin/python3
"""
Python script that posts an email
"""

import requests
import sys

if __name__ == "__main__":
    try:
        req = requests.get(sys.argv[1])
        print(req.text)
    except error.HTTPError:
        print("Error code: {}".format(req.status_code))
