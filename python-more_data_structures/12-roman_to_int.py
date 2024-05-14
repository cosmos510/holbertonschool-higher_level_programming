#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    result = 0
    last = 0
    my_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for letter in roman_string:
        if letter in my_dict:
            value = my_dict[letter]
            result += value
            if last < value:
                result -= 2 * last
            last = value
    return result
