#!/usr/bin/python3
"""
 class defined by it's size with a default value
"""


class Square:
    """
    defines the square class
    """

    def __init__(self, size, position=(0, 0)):
        """
        the initialized with the argument size
        """
        self.size = size
        self.position = position

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
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        position getter
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        position setter
        """
        if len(value) != 2 and type(value) is not tuple and type(value[0])\
           is not int and type(value[1]) is not int and value[0] <= 0\
           and value[1] <= 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        returns the area
        """
        return self.__size**2

    def my_print(self):
        """
        print the square with spaces and #
        """
        if self.__size == 0:
            print("\n")
        else:
            for i in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    print(" ", end='')
                for j in range(0, self.__size):
                    print("#", end='')
                print("\n", end='')
            if(self.__position[1]) > 0:
                print(" ", end='')
