#!/usr/bin/python3
"""
contains  MyList class
"""


class MyList(list):
    """subclass list"""
    def __init__(self):
        """constructor"""
        super().__init__()

    def print_sorted(self):
        """print  the sorted list"""
        print(sorted(list(self)))
