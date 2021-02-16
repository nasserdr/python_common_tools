#!/usr/bin/python3
"""
Read n lines
"""


def read_lines(filename="", nb_lines=0):
    """
    Reads nb_lines from filename
    """
    with open(filename, mode='r') as MyFile:
        if nb_lines <= 0:
            line_nb = 1
            while True:
                line = MyFile.readline()
                print(line, end='')
                line_nb = + 1
                if not line:
                    break
        else:
            for i in range(nb_lines):
                line = MyFile.readline()
                print(line, end='')
