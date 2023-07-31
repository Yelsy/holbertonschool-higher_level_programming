#!/usr/bin/python3
""" define a function that adds attributes to obj"""


def add_attribute(obj, att, value):
    """ add a new attrbute to an obj if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
