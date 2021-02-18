#!/usr/bin/python3
"""serialize a python object
"""
import json


def class_to_json(obj):
    """
    Return a json of obj
    """
    return json.loads(json.dumps(obj.__dict__))
