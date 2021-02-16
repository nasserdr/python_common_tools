#!/usr/bin/python3
"""
Checks exact same object
"""


def is_same_class(obj, a_class):
    """
    Check if the object of the same class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
