from numpy import zeros, arange, fabs
import matplotlib.pyplot as plt


def sweep(v, p, q, r, s):
    for i in range(1, len(v)-1):
        for j in range(1, len(v)-1):
            c = 0.0
            if i == p and j == q:
                c = 1.0
            if i == r and j == s:
                c = -1.0
            v[i, j] = 0.25 * (v[i - 1, j] + v[i + 1, j] + v[i, j - 1] + v[i, j+1] + c)


if __name__ == '__main__':
    N: int = 22
    v: list = zeros((N, N), float)
    p: int = int((len(v) - 1) / 2)
    q: int = int((len(v) - 1) / 2)
    r: int = p + 1
    s: int = p + 0
    dv: float = 1.0e10
    lastdv = 0
    count = 0
    while fabs(dv-lastdv) > 1.0e-7 * fabs(dv):
        lastdv = dv
        sweep(v, p, q, r, s)
        dv = v[p, q] - v[r, s]
        count += 1
    print(count, dv)
    plt.figure(figsize=(8, 8))
    plt.contour(v)
#    plt.savefig(f'./q7_1_{N-2}x{N-2}_AtoB.png')

