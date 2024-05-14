#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    ret = 0
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    for num in new_list:
        ret += num
    return (ret)
