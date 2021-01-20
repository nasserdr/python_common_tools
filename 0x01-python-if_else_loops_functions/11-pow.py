def pow(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    elif b < 0:
        pow = 1
        while (b < 0):
            pow *= a
            b += 1
        return 1/pow
    else:
        pow = 1
        while (b >= 1):
            pow *= a
            b -= 1
        return pow
