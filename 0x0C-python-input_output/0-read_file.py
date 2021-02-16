#!/usr/bin/python3
"""
Reading lines
"""


def read_file(filename=""):
    """
    Read all the lines in filename
    """
    with open('my_file_0.txt', 'r', encoding = "utf-8") as myFile:
        for lines in myFile:
            print(lines, end='')
