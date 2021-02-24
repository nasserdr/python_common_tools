#!/usr/bin/python3
"""
Minimum operations file
"""
from itertools import product
n = 4
target = 'H'*n
my_list = list()
big_list = list()
i = 0
min_op_list = None
min_op = n

p = list(product(['copy', 'paste'], repeat=n))

for s in p:
    my_list = list(s)
    big_list.append(my_list)

for l in big_list:
    l.insert(0, 'copy')
print(big_list)

for l in list:
    string = 'H'
    count = 0
    for case in l:
        if case == 'copy':
            to_be_added = string
        else:
            string = to_be_added*2
        count = count + 1

        if string == target:
            min_op_list.append(count)
