from math import cos
import copy
import matplotlib.pyplot as plt


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
            dt = 0.0015
            y = i
            startt = copy.copy(y)
            tf = 30.0
            nsteps = int(tf / dt)
            temp1 = []
            temp2 = []
            for i in range(nsteps):
                y = odestep(f, y, t, dt, w)
                t = (i + 1) * dt
                temp1.append(y)
                temp2.append(t)
            data.append([temp2, temp1])
        plt.plot(data[0][0], data[0][1])
        plt.plot(data[1][0], data[1][1])
        plt.plot(data[2][0], data[2][1])
        plt.xlabel('RC[s]')
        plt.xlabel('Voltage[V]')
        plt.savefig(f'./q6_6_t{startt}.png')
        plt.clf()
