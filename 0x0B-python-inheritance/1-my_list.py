#!/usr/bin/python3
class MyList(list):
    """
    The MyList Class
    """
    def print_sorted(self):
        """
        Returns list in ascending order
        """      
        self.sort()
        print(self)