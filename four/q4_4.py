from q4_1 import trap0
import numpy as np


def trap1(f, a, b, delta, maxtraps=512):
    '''Improved trapezium rule.
    Integrate f(x) over interval
    from a to b, trying to get relative
    accuracy delta. Optional last
    argument is maximum allowed number of trapezia.'''
    n = 8
    inew = trap0(f, a, b, n)
    iold = -inew
    while (np.fabs(inew - iold) > delta * np.fabs(inew)):
        iold = inew
        n = 2 * n
        if n > maxtraps:
            print('Cannot reach requested accuracy with',
                  maxtraps, 'trapezia')
            return
        inew = trap0(f, a, b, n)
    return inew


def fe(x):
    return np.e ** (-x ** 2)


if __name__ == '__main__':
    x = 10
    print(trap1(fe, -x, x, 1.0e-3))
