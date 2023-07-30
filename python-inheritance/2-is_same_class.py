#!/usr/bin/python3
"""checks if the object is a instance of a class"""


def is_same_class(obj, a_class):
    """function that return if the obj is isntance of the class
    otherwise false"""
    if type(obj) == a_class:
        return True
    else:
        return False
