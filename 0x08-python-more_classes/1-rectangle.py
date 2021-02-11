#!/usr/bin/python3
"""
 class to define a rectange
"""


class Rectangle:
    """
    defines the square class
    """
    def __init__(self, width=0, height=0):
        """
        initializes the classe rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        The getter"
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        the setter of the width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        The getter of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        the setter of the height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
