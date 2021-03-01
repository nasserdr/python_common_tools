#!/usr/bin/python3
""" method that determines if a given
data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    utf = True
    for i in data:
        if i >= 256:
            utf = not utf
            break
    return utf
