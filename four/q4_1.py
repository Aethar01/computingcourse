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


if __name__ == '__main__':
    n = 3
    a = [trap0(f, 0, 1, 1), trap0(f, 0, 1, 2)]
    while not np.fabs((a[-1] - a[-2])) < 1.0e-6:
        a.append(trap0(f, 0, 1, n))
        n += 1

    print('the integrals value is', a[-1])
    print(n)
