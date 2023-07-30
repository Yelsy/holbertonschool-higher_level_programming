#!/usr/bin/python3
"""width and height validation"""


class Rectangle:
    """class variable rectangle"""
    def __init__(self, width=0, height=0):
        """initialize width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """return the value"""
        return self.__width

    @width.setter
    def width(self, value):
        """validation of width if is an integer"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """return the value"""
        return self.width

    @height.setter
    def height(self, value):
        """validation of height if is an integer if not set the value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
