def squarroot(x):
    y = x
    while y * y != x:
        y = 0.5 * (y + x / y)
        print(y, y*y)
    return y


print(squarroot(2))
