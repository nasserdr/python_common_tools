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
            self.__size = size
            if type(self.__size) is not int or type(self.__size) is not float:
                raise TypeError
            if self.__size < 0:
                raise ValueError
        except ValueError:
            print('test1')
        except TypeError:
            print('test 2')
