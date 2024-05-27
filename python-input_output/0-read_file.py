#!/usr/bin/python3
"""
This module contains a function that reads a
text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """
        function that read a file
    """
    with open(filename, encoding="utf-8") as file_read:
        read_data = file_read.read()
    print(read_data, end="")
