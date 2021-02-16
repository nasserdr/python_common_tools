#!/usr/bin/python3
"""
Writes an Object to a text file
"""


def save_to_json_file(my_obj, filename):
    """
    Writes my_obj to filename
    """
    with open(filename, mode='w') as jsonfile:
        jsonfile.dunp(my_obj, filename)
