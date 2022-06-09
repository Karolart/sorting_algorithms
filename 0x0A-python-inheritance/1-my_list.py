#!/usr/bin/python3
"A module contains MyList class"


class MyList(list):
    """MyList class
    Attributes:
    attr1(print_sorted): prints sorted list
    """
    def print_sorted(self):
        """Prints instance"""
        print(sorted(self))
