#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square data that inherits from Rectangle"""
    
    def __init__(self, size):
        """square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Method to calculate area of the square"""

        return self.__size * self.__size
