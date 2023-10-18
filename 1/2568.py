from math import pi
import numpy as np
from numpy import random, cos, fabs
import matplotlib.pyplot as plt


def two():
    for i in range(1, 11):
        print(i, i**2, i**3)


def g(x):
    n = 1
    total = term = cos(x)  # First term
    while fabs(term) > (1.0e-7 * fabs(total) + 1.0e-13):
        n += 2  # Advance to next term
        term = cos(n * x) / (n * n)
        total += term  # Add term to total
    return total


def five():
    x = np.arange(0, 4*pi, 0.01)
    y = [g(i) for i in x]
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('g(x)')
    plt.xticks(ticks=[0, pi, 2 * pi, 3 * pi, 4 * pi], labels=['0', '$\pi$', '2$\pi$', '3$\pi$', '4$\pi$'])
    plt.savefig('1_5.png', dpi=300)


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


def six():
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


def next_node(r: float, s: float, R_i: list) -> float:
    return (r + s * R_i[-1] / (s + R_i[-1]))


def gen_data1(r: float, s: float) -> list:
    R_i = [r + s]
    while len(R_i) < 2 or (R_i[-2] - R_i[-1] >= 1e-7):
        R_i.append(next_node(r, s, R_i))
    return R_i


def eight():
    s = 10000.0
    r = 100.0
    R_i = gen_data1(r=r, s=s)
    print(R_i[-1])
    plt.plot(R_i)
    plt.savefig("1_8.png")


def main():
    which = input("Which question? (2, 5, 6, 8): ")
    match which:
        case "2":
            two()
        case "5":
            five()
        case "6":
            six()
        case "8":
            eight()
        case _:
            print("Invalid question number")


if __name__ == "__main__":
    main()
