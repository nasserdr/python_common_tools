#!/usr/bin/python3
"""
Mynt Class
"""


class MyInt(int):
    """
    class MyInt
    """
    def __init__(self, value):
        """
        initi
        """
        self.__value = value

    def __ne__(self, other):
        """
        overloading the not equal operator
        """
        return self.__value == other

    def __eq__(self, other):
        """
        overloading the  equal operator
        """
        return self.__value != other
