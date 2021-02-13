#!/usr/bin/python3
"""
Say my name software
"""


def say_my_name(first_name, last_name=""):
    """
    The say my name function
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    elif last_name == "":
        print("My name is {}".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
