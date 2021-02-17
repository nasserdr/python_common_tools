#!/usr/bin/python
"""
Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    The class square inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initializing the class
        """
        Rectangle.__init__(self, size, size)
