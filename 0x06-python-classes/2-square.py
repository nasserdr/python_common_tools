#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
A class defined by it's size with a default value
"""


class Square:
    """an empty class Square that defines a square """
    try:
        def __init__(self, size=0):
            """ To initialize the size of the squere"""
            self.__size = size
    except TypeError:
        print('size must be an integer')
    except ValueError:
        print('size must be >= 0')
