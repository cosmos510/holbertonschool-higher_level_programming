#!/usr/bin/python3

def print_last_digit(number):
    """Return last digit of number."""
    ld = abs(number) % 10
    print(f"{ld}", end="")
    return(ld)
