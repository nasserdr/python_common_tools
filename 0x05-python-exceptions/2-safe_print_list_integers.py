#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb = 0
    for i in range(0, x):
        try:
            print('{:d}'.format(my_list[i]), end='')
            nb += 1
        except (TypeError, ValueError, IndexError):
            continue
    print("")
    return nb
