#!/usr/bin/python3
"""
Finds a peak
"""
def find_peak(list_of_integers):
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        a = list_of_integers[0]
        b = list_of_integers[1]
        return a if a>b else b
    else:
        for l in range(1, len(list_of_integers)-1):
            a = list_of_integers[l-1]
            b = list_of_integers[l]
            c = list_of_integers[l+1]
            if b>=a and b>=c:
                peak = b
        if(peak):
            return peak
