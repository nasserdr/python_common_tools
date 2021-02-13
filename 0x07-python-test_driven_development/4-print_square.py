#!/usr/bin/python3
"""
Prints squares
"""


def print_square(size):
    """
    The function print_square
    """

    if type(size) is float and size < 0:
        raise TypeError("size must be >= 0")
    elif type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("")
