#!/usr/bin/python3
letters = []
for a in range(ord('a'), ord('z') + 1):
    letters.append(chr(a))

print(*letters, sep='', end='')

