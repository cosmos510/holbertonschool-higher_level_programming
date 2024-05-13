#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        pass
    elif idx not in range(len(my_list)):
        pass
    my_list[idx] = element
    return (my_list)
