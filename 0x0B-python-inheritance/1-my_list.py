#!/usr/bin/python3
"""
Sorting a list in ascending order via inheritance from the class list
"""


class MyList(list):
    """
    The MyList Class
    """
    def print_sorted(self):
        """
        Returns list in ascending order
        """
        new = sorted(self)
        print(new)
