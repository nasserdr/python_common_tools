#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for k, v in a_dictionary.items():
        new[k] = a_dictionary[k] * 2
    return new
