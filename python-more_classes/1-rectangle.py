#!/usr/bin/python3
"""width and height validation"""


class Rectangle:
    """class variable rectangle"""
    def __init__(self, width=0, height=0):
        """initialize width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """return the value"""
        return self.__width

    @width.setter
    def width(self, value):
        """validation of width if is an integer"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """return the value"""
        return self.__height

    @height.setter
    def height(self, value):
        """validation of height if is an integer if not set the value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
