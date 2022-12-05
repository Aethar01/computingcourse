from numpy import zeros, arange, fabs, sqrt
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
# import time


def sweep(v, p, q, r, s, a):
    for i in range(1, len(v)-1):
        for j in range(1, len(v)-1):
            c = 0.0
            if i == p and j == q:
                c = 1.0
            if i == r and j == s:
                c = -1.0
            v[i, j] = ((v[i + 1, j] + v[i - 1, j] + v[i, j + 1] + v[i, j - 1] + c) - a * v[i, j]) / (4 - a)


if __name__ == '__main__':
    N: int = 22
    v: list = zeros((N, N), float)
#    p: int = int((len(v) - 1) / 2)
#    q: int = int((len(v) - 1) / 2)
    p: int = 1
    q: int = 1
    r: int = 1
    s: int = 1
    a: float = 1.70006
    dv: float = 1.0e10
    lastdv = 0
    count = 0
    horizontaldist = [i for i in range(N-1)]
    vhor = []
    diagonaldist = [i * sqrt(2) for i in range(N-1)]
    vdiag = []

    for i in range(N-1):
        sweep(v, p, q, r, s, a)
        vhor.append(v[p, q] - v[r, s])
        r += 1

    p: int = 1
    q: int = 1
    r: int = 1
    s: int = 1

    for i in range(N-1):
        sweep(v, p, q, r, s, a)
        vdiag.append(v[p, q] - v[r, s])
        r += 1
        s += 1

    fig, ax = plt.subplots()
    horizontal, = ax.plot(horizontaldist, vhor, label='horizontal')
    diagonal, = ax.plot(diagonaldist, vdiag, label='diagonal')
    ax.legend(handles=[horizontal, diagonal])
    fig.suptitle('Comparison of voltage on nodes accross a 20x20 array')
    ax.set_ylabel('Voltage [V]')
    ax.set_xlabel('Distance from [0, 0] in nodes')
    plt.savefig('./q7_4.png')
