#!/usr/bin/python3
"""checks if the object is a instance of a class or an inherit class"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or
     inherited instance of a class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
