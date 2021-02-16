#!/usr/bin/python3
"""
returns True if the object is an instance of a class that inherited 
(directly or indirectly) from the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    Check if the object of the same class
    """
    return isinstance(obj, a_class)
