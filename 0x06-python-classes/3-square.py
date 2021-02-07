#!/usr/bin/python3
# -*- coding: utf-8 -*-
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
        try:
            if type(size) is not int:
                raise TypeError
            if size < 0:
                raise ValueError
            self.__size = size
        except ValueError:
            print('size must be >0')
        except TypeError:
            print('size must be an integer')

    def area(self):
        return self.__size**2
