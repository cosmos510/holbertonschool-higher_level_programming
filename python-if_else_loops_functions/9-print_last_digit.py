#!/usr/bin/python3

def print_last_digit(number):
    """Return last digit of number."""
    ld = abs(number) % 10
    print(ld, end="")
    return(ld)
