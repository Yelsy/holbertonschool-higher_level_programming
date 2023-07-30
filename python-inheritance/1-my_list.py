#!/usr/bin/python3
"""This class inherits from the list class"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """Prints a sorted class"""
        print(sorted(self))
