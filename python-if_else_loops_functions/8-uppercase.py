#!/usr/bin/python3
def uppercase(str):
    letter_up = ""
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            letter_up += chr(ord(letter) - 32)
        else:
            letter_up += letter
    print("{}".format(letter_up))
