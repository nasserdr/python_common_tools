#!/usr/bin/python3
c = 122
upper = False
while(c >= 97):
    if(upper is False):
        print('{}'.format(chr(c)), end='')
    else:
        print('{}'.format(chr(c-32)), end='')
    c -= 1
    upper = not upper
print('\n')
