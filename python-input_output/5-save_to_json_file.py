#!/usr/bin/python3
"""
    Module that create a function save_to_json
"""
import json


def save_to_json_file(my_obj, filename):
    """
        function that writes an Object to a text file,
        using a JSON representation
    """
    with open(filename, 'w', encoding="utf-8") as my_file:
        return json.dump(my_obj, my_file)
