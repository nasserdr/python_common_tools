#!/usr/bin/python3
"""
 class defined by it's size with a default value
"""


class Square:
    """
    defines the square class
    """

    def __init__(self, size=0):
        """
        the initialized with the argument size
        """
        self.size = size

    @property
    def size(self):
        """
        The getter property for the size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        The setter of the size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value <= 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        returns the area
        """
        return self.__size**2
