#!/usr/bin/python3
"""
    Module that create a function
"""


def append_after(filename="", search_string="", new_string=""):
    """
        function that inserts a line of text to a file,
        after each line containing a specific string
    """
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
    new_line = []
    for line in lines:
        new_line.append(line)
        if search_string in line:
            new_line.append(new_string)

    with open(filename, 'w', encoding="utf-8") as file:
        file.writelines(new_line)
