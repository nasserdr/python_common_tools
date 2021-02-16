#!/usr/bin/python3
"""
Counting lines
"""


def number_of_lines(filename=""):
    """
    Coun lines
    """
    with open(filename, 'r', encoding="utf-8") as myFile:
        n = 0
        for lines in myFile:
            n += 1
        return n
