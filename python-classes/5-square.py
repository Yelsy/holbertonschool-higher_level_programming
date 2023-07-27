#!/usr/bin/python3
"""size validation"""


class Square:
    """class variable size"""

    def __init__(self, size=0):
        """initialize size"""

        self.__size = size

    @property
    def size(self):
        """property to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter to set it"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """public instance method that returns area"""

        return self.__size * self.__size

    def my_print(self):
        """prints in stdout the square with the character #"""

        if self.__size > 0:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
