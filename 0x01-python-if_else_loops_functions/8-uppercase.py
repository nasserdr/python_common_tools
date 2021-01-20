def uppercase(str):
    s = ''
    for i in str:
        s = s + chr(ord(i) + 26)
    return s
