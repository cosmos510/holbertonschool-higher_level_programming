#!/usr/bin/python3
"""
    Module that create function from_json_string
"""
from json import JSONDecoder


def from_json_string(my_str):
    """
        function that returns an object
        (Python data structure) represented by a JSON string
    """
    return JSONDecoder().decode(my_str)
