from math import cos
from math import pi
import copy
from numpy import arange
import matplotlib.pyplot as plt
import scipy


def odestep(f, y, t, dt, w):
    dA = f(y, t, w)
    Bpr = y + dt * f(y, t, w)
    Bpry = f(Bpr, t, w)
    return y + 0.5 * (dA + Bpry) * dt


def g(w, t):
    return cos(w * t)


def f(y, t, w):
    return -y + g(w, t)


def counter():
    n = 0
    while True:
        yield n
        n += 1


if __name__ == '__main__':
    for i in counter():
        if i >= 11:
            break
        data: list = []
        for w in [0.5, 1, 2]:
            t = 0
            y = i
            dt = 0.0015
            startt = copy.copy(i)
            tf = 30.0
            nsteps = int(tf / dt)
            temp1 = []
            temp2 = []
            for x in range(nsteps):
                y = odestep(f, y, t, dt, w)
                t = (x + 1) * dt
                temp1.append(y)
                temp2.append(t)
            data.append([temp2, temp1])
        fig, (axs0, axs1, axs2) = plt.subplots(3, 1, sharex=True, sharey=True)
        axs0.plot(data[0][0], data[0][1])
        axs0.set_title('$\omega$ = 0.5')
        axs0.plot(arange(0, int(tf), 0.1), [f(0, t, 0.5) for t in arange(0, int(tf), 0.1)])
        axs1.plot(data[1][0], data[1][1])
        axs1.set_title('$\omega$ = 1')
        axs1.plot(arange(0, int(tf), 0.1), [f(0, t, 1) for t in arange(0, int(tf), 0.1)])
        axs2.plot(data[2][0], data[2][1])
        axs2.set_title('$\omega$ = 2')
        axs2.plot(arange(0, int(tf), 0.1), [f(0, t, 2) for t in arange(0, int(tf), 0.1)])
        axs = (axs0, axs1, axs2)
        for ax in axs:
            ax.set(ylabel='Voltage[V]', xlabel='RC[s]')

        fig.suptitle(f'When y(t=0) = {startt}')

        for ax in axs:
            ax.label_outer()
        plt.savefig(f'./q6_6_t{startt}.png')
        plt.clf()
        print(f'when y(t=o) is {startt}')
        print(max(data[0][1]))
        print(max(data[1][1]))
        print(max(data[2][1]))
        print(scipy.signal.correlate(data[0][1], [f(0, t, 0.5) for t in arange(0, int(tf), 0.1)])[data[0][1].index(max(data[0][1]))] % (2 * pi))
        print(scipy.signal.correlate(data[1][1], [f(0, t, 0.5) for t in arange(0, int(tf), 0.1)])[data[1][1].index(max(data[1][1]))] % 2 * pi)
        print(scipy.signal.correlate(data[2][1], [f(0, t, 0.5) for t in arange(0, int(tf), 0.1)])[data[2][1].index(max(data[2][1]))] % 2 * pi)
