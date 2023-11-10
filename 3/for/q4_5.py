from math import pi, cos, sin
from matplotlib import pyplot as plt
import numpy as np


def period(a, phi):
    return 1 / ((cos(phi) - cos(a)) ** 0.5)


def period1(phi, a):
    return 1 / (1 - (sin(a / 2) ** 2) * (sin(phi)) ** 2) ** 0.5


if __name__ == '__main__':
    x = np.linspace(-10, 10, 1000)
    y = [period(pi/4, i) for i in x]

    plt.plot(x, y)
    plt.savefig('q4_5.png')
    plt.clf()

    y1 = [period1(pi/4, i) for i in x]

    plt.plot(x, y1)
    plt.savefig('q4_6.png')
