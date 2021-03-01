#!/usr/bin/python3
"""
Python script access github
"""

import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    req = requests.get(url, auth=(sys.argv[1], sys.argv[2])).json()
    print(req.get('id'))
