#!/usr/bin/python3
def roman_to_int(roman_string):
    result = 0
    my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for letter in roman_string:
        if letter in my_dict:
            result += my_dict[letter]
    return result
