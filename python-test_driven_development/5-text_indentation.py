#!/usr/bin/python3
"""Module to cereate a function that prints new lines on . ? :"""


def text_indentation(text):
    """
        Function hat prints a text with 2 new lines
        after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for let in text:
        if let in ".?:":
            print("{}\n".format(let))
        else:
            print("{}".format(let), end='')
