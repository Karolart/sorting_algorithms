#!/usr/bin/python3
"""
Module for Defines a class Rectangle
"""


class Rectangle:
    """defines a rectangle"""
    def __init__(self, width=0, height=0):
        """constructor"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the data for the velue of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the data for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get the data for an instance of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the  rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """returns rectangle print representation"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string

    def __repr__(self):
        """returns a string representation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
