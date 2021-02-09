#!/usr/bin/python3
"""
A class defined by it's size with a default value
"""


class Square:
    """
    an empty class Square that defines a square
    """
    def __init__(self, size=0):
        """
        To initialize the size of the square
        """
        if type(size) is not int and type(size) is not float:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
