#!/usr/bin/python3
"""
A module to prints a list in ascending order
"""


class MyList(list):
    """
   initialize class
    """

    def print_sorted(self):
        """
        prints a sorted list 
        """

            print(sorted(self))
