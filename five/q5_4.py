from q5_1 import randbin1
import matplotlib.pyplot as plt

if __name__ == '__main__':
    maxrandnumbers = 1000
    bins = 10
    plt.bar([x/10 for x in range(bins)], randbin1(maxrandnumbers, bins), width=0.1, align='edge')
    plt.xticks([x/10 for x in range(bins + 1)])
    plt.savefig('./q5_4.png')
