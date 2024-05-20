#!/usr/bin/python3
"""Module to cereate a function that prints new lines on . ? :"""


def text_indentation(text):
    """
        Function hat prints a text with 2 new lines
        after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    skip_space = False
    for let in range(len(text)):
        if skip_space and text[let] == ' ':
            continue
        skip_space = False
        print("{}".format(text[let]), end='')
        if text[let] in ".?:":
            print("\n")
            skip_space = True
