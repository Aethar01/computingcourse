from math import cos, fabs, pi
import matplotlib.pyplot as plt
import numpy as np


def g(x):
    n = 1
    total = term = cos(x)
    while fabs(term) > (1.0e-7 * fabs(total) + 1.0e-13):
        n += 2
        term = cos(n * x) / (n * n)
        total += term
    return total


x = np.arange(0, 4*pi, 0.01)
y = [g(i) for i in x]
plt.plot(x, y)
plt.xlabel('x')
plt.xticks(ticks=[0, pi, 2 * pi, 3 * pi, 4 * pi], labels=['0', '$\pi$', '2$\pi$', '3$\pi$', '4$\pi$'])
plt.savefig('q1.png', dpi=300)
