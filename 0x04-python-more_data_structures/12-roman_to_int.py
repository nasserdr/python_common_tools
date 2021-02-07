#!/usr/bin/python3
def roman_to_int(roman_string):
    input = roman_string.upper()
    nums = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    sum = 0
    for i in range(len(input)):
        value = nums[input[i]]
        if i+1 < len(input) and nums[input[i+1]] > value:
            sum -= value
        else:
            sum += value
    return sum
