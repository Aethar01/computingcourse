from minimise import gmin
from numpy import exp


def f(x):
    return exp(x) + 1 / x


print(gmin(f, 0, 5, tol=3.0e-8))
