import matplotlib.pyplot as plt
from numpy import zeros, random


def randbin(totalrandnumbers, numofbins):
    m = zeros(numofbins, int)
    for i in range(totalrandnumbers):
        n = random.randint(numofbins)
        m[n] = m[n] + 1
    return m


def randbin1(totalrandomnumbers, totalbins, average=1):
    m = zeros(totalbins, int)
    for i in range(totalrandomnumbers):
        n = sum([random.random() for x in range(average)]) / average
        k = int(totalbins * n)
        m[k] = m[k] + 1
    return m


def normalgen(totalrandomnumbers):
    m: list = []
    for i in range(totalrandomnumbers):
        k = random.normal()
        m.append(k)
    return m


if __name__ == '__main__':
    maxrandnumbers = 1000
    bins = 10
    plt.bar([x/10 for x in range(bins)], randbin1(maxrandnumbers, bins), width=0.1, align='edge')
    plt.xticks([x/10 for x in range(bins + 1)])
    plt.xlabel('Random number value')
    plt.ylabel('Frequency Density')
    plt.savefig('./q5_4.png')
