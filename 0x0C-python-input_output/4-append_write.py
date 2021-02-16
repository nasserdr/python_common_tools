#!/usr/bin/python3
"""
Append a file
"""


def append_write(filename="", text=""):
    """
    Append filename with text
    """
    with open(filename, mode='a', encoding='utf-8') as MyFile:
        MyFile.write(text)
        return(len(text))
