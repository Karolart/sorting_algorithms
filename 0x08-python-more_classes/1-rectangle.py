#!/usr/bin/python3
"""
A module with a Rectangle that does nothing for a while
"""


class Rectangle:
    """ defines a rectangle class """

    def __init__(self, width=0, height=0):
        """
        constructor
        contain the parameters and initializes  values
        Args:
            width (:obj:`int`, optional): Rectangle width
            height (:obj:`int`, optional): Rectangle height
        """
        
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if type(value) not in [int]:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ get the data for heigth value """
        return self.height

    @height.setter
    def height(self, value):
        """ set the data for height value """

        if type(value) not in [int]:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
