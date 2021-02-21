#!/usr/bin/python
"""
The suqare class
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    The square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)
        self.size = size
    
    def __str__(self):
        """
    Prints the string representation of the square
    """
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.width)
    
    @property
    def size(self):
        """
        Size getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter with type and value validation
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__size = value
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """
        update the rectangle attributes using args
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.__size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionnary rep of the rectangle
        """
        return {'id': self.id, 'x': self.x,  'size': self.__size, 'y': self.y}