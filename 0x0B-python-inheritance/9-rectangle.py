#!/usr/bin/python3
"""Retangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    The class rectangle that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializing the class
        """
        try:
            self.integer_validator("width", width)
            self.__width = width
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

        try:
            self.integer_validator("height", height)
            self.__height = height
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))

    def area(self):
        return self.__width*self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
