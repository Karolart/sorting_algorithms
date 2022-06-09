#!/usr/bin/python3
"""
this module contains MyList class
"""


class MyList(list):
    """subclass list"""
    def __init__(self):
        """constructor"""
        super().__init__()

    def print_sorted(self):
        """prints the list sorted"""
        print(sorted(self))
