#!/usr/bin/python3
"""
Contains the read_file function
"""


def read_file(filename=""):
    """""read file(UTF8) file and  prints stdout"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
