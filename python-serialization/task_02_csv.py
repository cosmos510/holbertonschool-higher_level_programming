#!/usr/bin/python3
"""
    Module that reading data from one format (CSV) and
    converting it into another format (JSON)
    using serialization techniques.
"""
import csv
import json


def convert_csv_to_json(filename):
    """
        takes the CSV filename as its parameter and writes the JSON
    """
    file_json = "data.json"
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
        with open(file_json, 'w', encoding="utf-8") as json_file:
            json.dump(rows, json_file)
        return True
    except Exception:
        return False
