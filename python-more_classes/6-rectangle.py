#!/usr/bin/python3
"""width and height validation"""


class Rectangle:
    """class variable rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialize width and height"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Define area"""
        return self.__width * self.__height

    def perimeter(self):
        """Define perimeter"""
        if self.__width == 0 or self.height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """Prints the rectangle using #"""
        if self.__width == 0 or self.height == 0:
            return ("")
        sq = ""
        for column in range(self.__height):
            for row in range(self.__width):
                sq += "#"
            if column < self.__height - 1:
                sq += "\n"
        return sq

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """prints a message for every object that is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
