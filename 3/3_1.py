import numpy as np
import math
import matplotlib as plt


def f(x):
    return (x ** 4 * ((1 - x) ** 4) / (1 + (x ** 2)))


def trap0(f, a, b, n):
    '''Basic trapezium rule. Integrate f(x) over the
    interval from a to b using n strips.'''
    h: float = (b - a) / n
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


def fe(x):
    return np.e ** (-x ** 2)


def period(a, phi):
    return 1 / ((math.cos(phi) - math.cos(a)) ** 0.5)


def period1(phi, a):
    return 1 / (1 - (math.sin(a / 2) ** 2) * (math.sin(phi)) ** 2) ** 0.5


def q3_5():
    x = np.linspace(-10, 10, 1000)
    y = [period(math.pi/4, i) for i in x]

    plt.plot(x, y)
    plt.savefig('3_5.png')
    plt.clf()

    y1 = [period1(math.pi/4, i) for i in x]

    plt.plot(x, y1)
    plt.savefig('3_6.png')
    return None


def q3_1_to_4():
    n = 2
    a = [trap0(f, 0, 1, 1)]
    while len(a) < 2 or not np.fabs((a[-1] - a[-2])) < 1.0e-6:
        if n == 0 or n == 1:
            break
        else:
            a.append(trap0(f, 0, 1, n))
            n += 1

    print('the integrals value is', a[-1])
    print(n)

    print(f"Values for integral of e^'{'x^2'}' over a range of -1, 1 to -10, 10, increasing by 2 each time: {[trap1(fe, -x, x, 1.0e-3) for x in range(1, 11)]}")
    return None


if __name__ == "__main__":
    q3_1_to_4()
    q3_5()
