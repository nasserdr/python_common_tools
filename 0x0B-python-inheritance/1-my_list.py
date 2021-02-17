#!/usr/bin/python3
"""
Return a sorted list
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
        return new
