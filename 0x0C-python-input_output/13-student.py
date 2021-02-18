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
            'age': self.age,
            'last_name': self.last_name,
            'first_name': self.first_name
        }

    def reload_from_json(self, json):
        """
        Replace students
        """
        keys, values = json.keys(), json.values()
        for k, v in keys, values:
            setattr(self, k, v)
