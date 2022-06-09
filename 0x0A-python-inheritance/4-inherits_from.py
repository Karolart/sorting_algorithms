#!/usr/bin/python3
"""
this module cointains an inherits_from(obj, a_class) function ,it checks if theobject is an instance of a class
""

def inherits_from(obj, a_class):
    """
    This function returns True or False
    """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
