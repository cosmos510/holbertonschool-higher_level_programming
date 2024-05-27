#!/usr/bin/python3
"""
    Module that create a function append_write
"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding="utf-8") as file:
        nb_ch = file.write(text)
    return nb_ch
