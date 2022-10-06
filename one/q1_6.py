from math import sqrt


def a(x):
    return x-sqrt(x*x-1)


def b(x):
    return 1/(x + sqrt(x*x-1))


for i in range(150000, 150010):
    print(a(i), b(i))
