from numpy import random
import matplotlib.pyplot as plt


def gen_data(samples: int, _range: int) -> list:
    m: list = []
    for i in range(samples):
        n = random.random() * _range
        m.append(n)
    return m


def sort_to_bins(data, binsNo: int, _range: int) -> list:
    bins = [0 for bins in range(binsNo)]
    for x in data:
        bins[int(x * binsNo)] += 1
    return bins


if __name__ == "__main__":
    samples = 1000
    binsNo = 10
    _range = 1
    binnedData = sort_to_bins(gen_data(samples, _range), binsNo, _range)
    print(binnedData)
    plt.title("Binned data from random.random")
    plt.xticks(range(binsNo + 1), labels = [str(x * _range) for x in range(binsNo + 1)])
    plt.xlabel("Bins")
    plt.ylabel("Counts")
    plt.bar(range(binsNo), binnedData, width=0.9, align='edge')
    plt.savefig("1_6.png")
