import matplotlib.pyplot as plt
import numpy as np
from math import pi
four = __import__('1_4')


if __name__ == "__main__":
    x = np.arange(0, 4*pi, 0.01)
    y = [four.g(i) for i in x]
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('g(x)')
    plt.xticks(ticks=[0, pi, 2 * pi, 3 * pi, 4 * pi], labels=['0', '$\pi$', '2$\pi$', '3$\pi$', '4$\pi$'])
    plt.savefig('q1_5.png', dpi=300)
