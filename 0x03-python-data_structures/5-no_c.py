#!/usr/bin/python3
def no_c(my_string):
    new_s = ''
    for s in range(len(my_string)):
        if my_string[s] != 'c' and my_string[s] != 'C':
            new_s += my_string[s]
    return new_s
