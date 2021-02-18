#!/usr/bin/python3
"""
The student class
"""
class_to_json = __import__('10-class_to_json').class_to_json

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

    def to_json(self):
        """
        Transforms to json
        """
        return class_to_json(self)
