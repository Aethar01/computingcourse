from q4_4 import trap1
import numpy as np
from math import pi, sin
from matplotlib import pyplot as plt


def period2(phi):
    return 1 / (1 - (sin(a / 2) ** 2) * (sin(phi)) ** 2) ** 0.5


if __name__ == '__main__':
    global a
    alphas = np.linspace(0, 4 * pi, 100)
    q = []
    for a in alphas:
        q.append([a, trap1(period2, 0, pi / 2, 1.0e-3)])
    for x in q:
        print(f'for alpha {x[0]}, the ratio is {x[1] * 2 / pi}')

    plt.plot(alphas, [i[1] for i in q])
    plt.savefig('q4_7.png')
