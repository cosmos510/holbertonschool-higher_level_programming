#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    com = set_1 & set_2
    new_set = set()
    for i in set_1:
        if i not in com:
            new_set.add(i)
    for j in set_2:
        if j not in com:
            new_set.add(j)
    return new_set
