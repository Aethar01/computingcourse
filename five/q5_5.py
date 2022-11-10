from q5_1 import randbin1
import matplotlib.pyplot as plt


def generatedata(mean, totalnums, bins):
    data = randbin1(totalnums, bins, mean)
    datarange = [x/bins for x in range(bins)]
    return data, datarange


if __name__ == '__main__':
    x = []
    for i in range(1, 5):
        x.append(generatedata(i, 5000, 50))
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].bar(x[0][1], x[0][0], width=0.1, align='edge')
    axs[0, 0].set_title('Average with 1 sample')
    axs[0, 1].bar(x[1][1], x[1][0], width=0.1, align='edge')
    axs[0, 1].set_title('Average with 2 samples')
    axs[1, 0].bar(x[2][1], x[2][0], width=0.1, align='edge')
    axs[1, 0].set_title('Average with 3 samples')
    axs[1, 1].bar(x[3][1], x[3][0], width=0.1, align='edge')
    axs[1, 1].set_title('Average with 4 samples')
    for ax in axs.flat:
        ax.set(xlabel='Random number value', ylabel='Frequency Density')

    for ax in axs.flat:
        ax.label_outer()

    plt.savefig('./q5_5.png')
