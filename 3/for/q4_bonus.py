import sympy as sym
import numpy as np
from matplotlib import pyplot as plt
import bisect


# having a gander at algebraic integration in python

x = sym.Symbol('x')
theta = sym.Symbol('theta')
a = sym.Symbol('a')
# y = sym.integrate(sym.exp(-x ** 2), (x, -sym.oo, sym.oo))
# print(y)


integ = sym.Integral(1 / ((1 - sym.sin(a / 2) ** 2 * (sym.sin(theta) ** 2)
                           ) ** 0.5), (theta, 0, np.pi/2))
alphas = np.linspace(0, 4 * np.pi, 5000)
alphas = list(alphas)
bisect.insort(alphas, np.pi)
bisect.insort(alphas, 3 * np.pi)

k = integ.doit()
q = []
for alpha in alphas:
    q.append([alpha, 2 / np.pi * k.subs(a, alpha)])
plt.plot(alphas, [i[1] for i in q])
plt.xticks(ticks=[0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi], labels=['0',
                        '$\pi$', '2$\pi$', '3$\pi$', '4$\pi$'])
plt.savefig('q4_bonus.png')

# find exact value of amplitude 90 deg
print(2 / np.pi * k.subs(a, np.pi/2))
