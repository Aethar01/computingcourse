from q4_1 import trap1
import numpy as np
from math import pi, sin
from matplotlib import pyplot as plt
from tabulate import tabulate


def period2(phi):
    return 1 / (1 - (sin(a / 2) ** 2) * (sin(phi)) ** 2) ** 0.5


if __name__ == '__main__':
    global a
    alphas = np.linspace(0, 4 * pi, 1000)
    q = []
    for a in alphas:
        q.append([a, trap1(period2, 0, pi / 2, 1.0e-3)])
#        print(f'for alpha {x[0]}, the ratio is {x[1] * 2 / pi}')
    print(tabulate(q, headers=['alpha', 'ratio']))

    plt.plot(alphas, [i[1] for i in q])
    plt.xticks(ticks=[0, pi, 2 * pi, 3 * pi, 4 * pi], labels=['0',
                            '$\pi$', '2$\pi$', '3$\pi$', '4$\pi$'])
    plt.savefig('q4_7.png')

    q1 = q.copy()
    for x in q1:
        x[0] = round(x[0], 2)

    q1 = np.array(q1)
    condition1, condition2 = list(np.where(q1 == 1.57))
    condition1 = int(condition1)
    condition2 = int(condition2 + 1)
    print(f'when amplitude is at roughly pi/2, the value of \
T/T_0 is { 2 / pi * q1[condition1][condition2] }')
