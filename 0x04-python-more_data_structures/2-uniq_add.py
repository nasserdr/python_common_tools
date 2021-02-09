#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = my_list[0]
    if len(my_list) == 1:
        return sum
    else:
        for i in range(1, len(my_list)):
            if my_list[i] not in my_list[0:i]:
                sum += my_list[i]
    return sum
