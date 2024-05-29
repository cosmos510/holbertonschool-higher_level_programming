#!/usr/bin/python3
"""
    Module that serialization and deserialization
    using XML as an alternative format to JSON.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
        take a Python dictionary and a filename as parameters.
        It serialize the dictionary into XML and save it to the given filename.
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        ET.SubElement(root, key).text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
        take a filename as parameter.
        It deserializes the content of the file into a Python dictionary.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    return {element.tag: element.text for element in root}
