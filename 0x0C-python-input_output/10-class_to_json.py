#!/usr/bin/python3
"""serialize a python object
"""
import json


def class_to_json(obj):
    """
    Return a json of obj
    """
    try:
        return obj.toJSON()
    except:
        return obj.__dict__
