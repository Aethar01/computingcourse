from numpy import zeros, arange, fabs
import matplotlib.pyplot as plt
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
    p: int = int((len(v) - 1) / 2)
    q: int = int((len(v) - 1) / 2)
    r: int = p + 1
    s: int = p + 1
    a: float = 1.70006
    dv: float = 1.0e10
    lastdv: float = 0
    count: int = 0
    found: bool = False
    for a in arange(1.7, 2, 0.00001):
#        while fabs(dv-lastdv) > 1.0e-7 * fabs(dv):
        if not found:
            lastdv = dv
            sweep(v, p, q, r, s, a)
            dv = v[p, q] - v[r, s]
            count += 1
            if fabs(dv - 0.6364830) < 1.0e-3 * fabs(dv):
#            if fabs(dv - 0.4999245680561941) < 1.0e-3 * fabs(dv):
                found = True
                print(f'break at {a}')
                break
        if found:
            break
    print(count, dv)
#    plt.figure(figsize=(8, 8))
#    plt.contour(v)
#    plt.savefig(f'./q7_1_{N-2}x{N-2}_AtoC.png')

