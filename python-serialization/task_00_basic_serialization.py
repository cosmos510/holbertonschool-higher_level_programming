#!/usr/bin/python3
"""
    Module that Create a basic serialization module that adds
    the functionality to serialize a Python dictionary to a
    JSON file and deserialize the JSON file to recreate the Python Dictionary.
"""
import json
from json import JSONDecoder


def serialize_and_save_to_file(data, filename):
    """
        Function serialize and save data to the specified file
    """
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
        Function that load and deserialize data from the specified file
    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
