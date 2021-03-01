#!/usr/bin/python3
"""
that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a
parameter
"""

import requests
import sys

if __name__ == "__main__":
    try:
        req = requests.get(sys.argv[1])
        print(req.text)
    except error.HTTPError:
        print("Error code: {}".format(req.status_code))
