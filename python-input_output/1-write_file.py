#!/usr/bin/python3
"""
    Module that create a function write_files
"""


def write_file(filename="", text=""):
    """
        function that writes a string to a text file (UTF8)
        and returns the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        writed = file.write(text)
    return writed
