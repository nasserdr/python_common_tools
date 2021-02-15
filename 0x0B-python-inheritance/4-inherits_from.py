#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    Return true if obj inerits from a_class
    """
    return issubclass(type(obj), a_class)
