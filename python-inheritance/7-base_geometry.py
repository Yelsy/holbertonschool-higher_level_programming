#!/usr/bin/python3
"""An empty class"""


class BaseGeometry:
    """Define class represent BaseGeometry"""
    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if value is integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
