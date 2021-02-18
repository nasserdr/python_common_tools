#!/usr/bin/python3
"""
The student class
"""


class Student:
    """
    Here we define and develop the student class
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialiser
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Transforms to json
        """
        if type(attrs) == list:
            values = [x for x in attrs]
            return dict(zip(attrs, values))
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age}
