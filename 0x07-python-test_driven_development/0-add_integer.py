#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds 98 to the integer a
    """

    if type(a) in [float, int]:
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if type(b) in [float, int]:
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a+b
