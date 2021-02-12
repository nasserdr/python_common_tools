#!/usr/bin/python3
"""
To test it:
>>> add_integer(5,10)
15
"""


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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    doctest.testfile('tests/0-add_integer.txt')
