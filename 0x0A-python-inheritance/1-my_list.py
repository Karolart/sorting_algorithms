#!/usr/bin/python3
"""
contains  MyList class
"""


class MyList(list):
    """subclass list"""
      pass

    def print_sorted(self):
        """print  the sorted list"""
       
        if issubclass(MyList, list):
            print(sorted(self))
