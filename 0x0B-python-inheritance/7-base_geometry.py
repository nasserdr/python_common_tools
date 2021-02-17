#!/usr/bin/python3
class BaseGeometry:
    """
    Geometry class
    """
    def area(self):
        """
        raises exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
