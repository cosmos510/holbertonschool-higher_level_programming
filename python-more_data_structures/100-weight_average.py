#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    weight = 0
    div = 0
    for i in my_list:
        res = i[0] * i[1]
        weight += res
        div += i[1]
    return weight / div
