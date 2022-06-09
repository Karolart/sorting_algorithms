#!/usr/bin/python3
"""
it contains a is_same_class function
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj (any): The object to compare
        a_class (any): The class to compare with the object

    Returns True if obj is same instance, else False
    """

    return type(obj) is a_class
      
