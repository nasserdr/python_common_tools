#!/usr/bin/python3
"""serialize a python object
"""


def class_to_json(obj):
    """
    Return a json of obj
    """
    return obj.__dict__
