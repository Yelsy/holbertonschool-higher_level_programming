#!/usr/bin/python3
"""returns the list of available attributes
    and methods of an object"""


def lookup(obj):
    """This functions looks out for all attributes and methods of an object"""
    return dir(obj)
