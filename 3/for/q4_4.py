from q4_1 import trap1
import numpy as np


def fe(x):
    return np.e ** (-x ** 2)


if __name__ == '__main__':
    x = 10
    print(trap1(fe, -x, x, 1.0e-3))
