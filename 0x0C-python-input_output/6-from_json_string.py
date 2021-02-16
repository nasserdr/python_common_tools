#!/usr/bin/python3
"""
Create object from JSON
"""
import json


def from_json_string(my_str):
    """
    Creates an object from json
    """
    return json.loads(my_str)
