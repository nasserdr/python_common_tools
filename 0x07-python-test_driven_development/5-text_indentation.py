#!/usr/bin/python
"""
The indentation software
"""


def text_indentation(text):
    """
    The ind function
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        for i in range(0, len(text)):
            if text[i] in [':', '?', '.']:
                print("\n")
            else:
                print(text[i], end='')
