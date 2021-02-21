#!/usr/bin/python3
"""
Whether we can add attributes
"""


def add_attribute(obj, name, value):
    """
    Checks whether we can add an attribute
    """
    if hasattr(obj, name):
        setattr(obj, name, value)
    else:
        raise TypeError("cant add new attribute")
