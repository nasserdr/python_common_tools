#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = [0 for x in my_list]
    for i in range(len(my_list)):
        if my_list[i] == search:
            new[i] = replace
        else:
            new[i] = my_list[i]
    return new
