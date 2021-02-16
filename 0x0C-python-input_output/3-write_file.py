#/usr/bin/python3
"""
Writing in a file
"""


def write_file(filename="", text=""):
    """
    writes text in filename
    """
    with open(filename, mode='w', encoding='UTF-8') as MyFile:
        MyFile.write(text)
        return(len(text))
