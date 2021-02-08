#!/usr/bin/python3
def remove_char_at(str, n):
    str_new = ''
    for s in range(0, len(str)):
        if s != n:
            str_new = str_new + str[s]
    return str_new
