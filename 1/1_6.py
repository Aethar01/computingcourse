from numpy import random, zeroes
import matplotlib.pyplot as plt


def gen_data(samples: int):
    m: list = []
    for i in range(samples):
        n = random.random()
        m.append(n)
    return m


def sort_to_bins(data, bins: list):
    


if __name__ == "__main__":
    samples = 10000
    bins = 10
    data = sort_to_bins(gen_data(samples, bins), 10)
    print(data)
    plt.bar(range(10), data, width=1, align='center')
