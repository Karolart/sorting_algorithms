#!/usr/bin/python3
"""
module for a Rectangle class definition 
"""


class Rectangle:
    """class of a rectangle"""
    def __init__(self, width=0, height=0):
        """constructor for initializes a rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the data for the private width instance attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """set the data for the private width instance attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the data for the private height instance attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the data for the private height instance attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
