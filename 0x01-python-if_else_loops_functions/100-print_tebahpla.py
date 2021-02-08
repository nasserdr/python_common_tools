#!/usr/bin/python3
c = 122
upper = False
while(c >= 97):
    print('{}'.format(chr(c-32*upper)), end='')
    c -= 1
    upper = not upper
