#!/usr/bin/python3
"""
Contains the number_of_lines function
"""


def number_of_lines(filename=""):
    """returns the number of lines of a text file"""
    with open(filename, "r", encoding="UTF-8") as f:
        return len(list(f))
