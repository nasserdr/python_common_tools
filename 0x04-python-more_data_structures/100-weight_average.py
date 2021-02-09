#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        w = 0
        sum = 0
        for t in my_list:
            sum += t[0]*t[1]
            w += t[1]
    return sum/w
