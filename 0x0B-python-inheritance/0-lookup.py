#!/usr/bin/python3
"""
List of arguments and methods in an object
"""


def lookup(obj):
    """
    Output the list of arguments and methods that belongs to the obj
    """
    return dir(obj)
