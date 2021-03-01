#!/usr/bin/python3
"""
that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a
parameter
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        payload = {'q': sys.argv[1]}
        req = requests.post("http://0.0.0.0:5000/search_user", payload)
        if req['content-type'] == 'application/json':
            print(req.text)
        elif req.text == "":
            print("No result")
        else:
            print("Not a valid JSON")
    else:
        print("No result")
