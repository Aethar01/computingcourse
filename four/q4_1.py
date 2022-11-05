import numpy as np


def f(x):
    return (x ** 4 * ((1 - x) ** 4) / (1 + (x ** 2)))


def trap0(f, a, b, n):
    '''Basic trapezium rule. Integrate f(x) over the
    interval from a to b using n strips.'''
    h = float(b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s = s + f(a+i*h)
    return s*h


if __name__ == '__main__':
    n = 3
    a = [trap0(f, 0, 1, 1), trap0(f, 0, 1, 2)]
    while not np.fabs((a[-1] - a[-2])) < 1.0e-6:
        a.append(trap0(f, 0, 1, n))
        n += 1

    print('the integrals value is', a[-1])
    print(n)
