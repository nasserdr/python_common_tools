#!/usr/bin/python3
"""
Python script that posts an email
"""

import requests
import sys

if __name__ == "__main__":
    payload = {'email': argv[2]}
    req = requests.post(argv[1], payload)
    print(req.text)
