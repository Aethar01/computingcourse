import numpy as np
import math
import matplotlib.pyplot as plt


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
    plt.savefig('3_5_2.png')
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


def q3_6():
    global a # required since trap1() uses a single variable whereas period2() uses two, a and phi
    alphas = np.linspace(0, 4 * math.pi, 1000)
    q = []

    def period2(phi):
        return 1 / (1 - (math.sin(a / 2) ** 2) * (math.sin(phi)) ** 2) ** 0.5

    for a in alphas:
        q.append([a, trap1(period2, 0, math.pi / 2, 1.0e-3)])

    for i in q:
        try:
            i[1] = i[1] * 2 / math.pi
        except TypeError:
            pass

    print('alpha \t ratio')
    for i in q:
        print(f'{i[0]} \t {i[1]}')

    plt.plot(alphas, [i[1] for i in q])
    plt.xticks(ticks=[0, math.pi, 2 * math.pi, 3 * math.pi, 4 * math.pi], labels=['0', '$\pi$', '2$\pi$', '3$\pi$', '4$\pi$'])
    plt.savefig('3_6.png')

    q1 = q.copy()
    for x in q1:
        x[0] = round(x[0], 2)

    q1 = np.array(q1)
    condition1, condition2 = list(np.where(q1 == 1.57))
    condition1 = int(condition1)
    condition2 = int(condition2 + 1)
    print(f'when amplitude is at roughly pi/2, the value of \
T/T_0 is {q1[condition1][condition2]}')


def q3_scipy():
    from numpy import log, sqrt
    from scipy.integrate import quad

    def f(x):
        return x ** 4 * log(x+sqrt(x**2+1))

    quad(f, 0, 2)


def q3_8():
    from scipy import stats

    def rand(xmin, ymin, xmax, ymax, n=1000):
        x = np.random.uniform(xmin, xmax, n)
        y = np.random.uniform(ymin, ymax, n)
        return (x, y)

    def norm():
        mu = 0
        variance = 1
        sigma = math.sqrt(variance)
        x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
        return (x, stats.norm.pdf(x, mu, sigma))

    samplesize = 10000
    xmin, ymin, xmax, ymax = -3, 0, 3, 1
    x, y = rand(xmin, ymin, xmax, ymax, samplesize)
    count_under = 0
    count_over = 0
    tempa = []
    tempb = []
    for i, x in zip(range(samplesize), x):
        if not y[i] > stats.norm.pdf(x, 0, 1) and -2 < x < 2:
            tempb.append((x, y[i]))
            # plt.scatter(x, y[i], color='red')
            count_under += 1
        else:
            tempa.append((x, y[i]))
            # plt.scatter(x, y[i], color='blue')
            count_over += 1

    plt.scatter(*zip(*tempa), color='blue')
    plt.scatter(*zip(*tempb), color='red')

    print(f'Ratio of points under the curve and within 2 sigma of the mean to all points is {count_under / (count_under + count_over)}')
    print(f'Area of the curve is {count_under / (count_under + count_over) * 6}')
    plt.plot(*norm())
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.savefig('3_8.png')

    from scipy.integrate import quad
    print(f'Actual value of integral is {quad(stats.norm.pdf, -2, 2)}')


if __name__ == "__main__":
    q3_1_to_4()
    plt.clf()
    q3_5()
    plt.clf()
    q3_6()
    plt.clf()
    q3_8()
