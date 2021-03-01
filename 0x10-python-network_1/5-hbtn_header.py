#!/usr/bin/python3
"""
Python script that fetches X-Request-Id from
https://intranet.hbtn.io/status
"""

import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers['X-Request-Id'])
