#!/usr/bin/python3
"""
Loads json from a file
"""
import json


def load_from_json_file(filename):
    """
    Loads JSON object from filename
    """
    with open(filename, mode='r') as jsonfile:
        return json.load(jsonfile)
