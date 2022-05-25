#!/usr/bin/python3
"""contains a definition of Square class"""



class Square:
    """attributes:
           __size(int): Square size side
    """
    def __init__(self, size=0):
        """initialized Square
           size(int) : Square size side
           Returns:
               none
        """   
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
