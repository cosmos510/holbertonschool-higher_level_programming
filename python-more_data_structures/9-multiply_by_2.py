#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for keys, values in new_dict.items():
        new_dict.update({keys: 2 * values})
    return new_dict
