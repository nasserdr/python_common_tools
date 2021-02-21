#!/usr/bin/python3
"""
Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class, it inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor
        """
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Width getter
        """
        return self.__width

    @property
    def height(self):
        """
        Height getter
        """
        return self.__height

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        width setter with type and value validation
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Height setter with type and value validation
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        """
        x setter with type and value validation
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        """
        y setter with type and value validation
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """
        returns the area of the rectangle:
        """
        return self.__width*self.__height

    def display(self):
        """
        prints the # representation of the rect
        """
        s = ''
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                s += "#"
            s += "\n"
        print(s[:-1])

    def __str__(self):
        """
        Prints the string representation of the retangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.__x,
            self.__y,
            self.__width,
            self.__height)

    def display(self):
        """
        print the square taking into account the position
        """
        for i in range(0, self.__y):
            print("\n", end='')
        for i in range(0, self.__height):
            for k in range(0, self.__x):
                print(" ", end='')
            for j in range(0, self.__width):
                print("#", end='')
            print("\n", end='')
        if(self.__y) > 0:
            print(" ", end='')


    # def update(self, *args):
    #     """
    #     update the rectangle attributes using args
    #     """
    #     if len(args) >= 1:
    #         self.id = args[0]
    #     if len(args) > 1:
    #         self.width = args[1]
    #     if len(args) > 2:
    #         self.height = args[2]
    #     if len(args) > 3:
    #         self.x = args[3]
    #     if len(args) > 4:
    #         self.y = args[4]
 

    def update(self, *args, **kwargs):
        """
        Update arguments from a key-value list
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionnary rep of the rectangle
        """
        return {'x': self.__x, 'y': self.__y, 'id': self.id, 'height': self.__height, 'width': self.__width}