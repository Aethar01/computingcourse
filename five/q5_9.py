from numpy import random, zeros
import matplotlib.pyplot as plt


def poissonsetgen(total: int, bins: int, mean: float):
    m = zeros(bins, int)
    n1 = random.poisson(mean, total)
    n = [x for x in n1 if x < bins]
#   a = mean / bins
    for i in n:
        #        k = int(i * a)
        m[i] = m[i] + 1
    datarange = [x for x in range(bins)]
    return m, datarange


if __name__ == '__main__':
    x = []
    for i in [2, 4, 6, 8]:
        x.append(poissonsetgen(5000, 25, i))

    fig, axs = plt.subplots(2, 2)
    axs[0, 0].bar(x[0][1], x[0][0], width=1, align='edge')
    axs[0, 0].set_title('Poisson with mean 2')
    axs[0, 1].bar(x[1][1], x[1][0], width=1, align='edge')
    axs[0, 1].set_title('Poisson with mean 4')
    axs[1, 0].bar(x[2][1], x[2][0], width=1, align='edge')
    axs[1, 0].set_title('Poisson with mean 6')
    axs[1, 1].bar(x[3][1], x[3][0], width=1, align='edge')
    axs[1, 1].set_title('Poisson with mean 8')
    for ax in axs.flat:
        ax.set(xlabel='Random number value', ylabel='Frequency Density')

    for ax in axs.flat:
        ax.label_outer()

    plt.savefig('./q5_9.png')
