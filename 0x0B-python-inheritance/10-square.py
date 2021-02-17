#!/usr/bin/python3
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
        try:
            Rectangle.__init__(self, size, size)
        except Exception as e:
            print("[{}] {}".format(e.__class__.__name__, e))
