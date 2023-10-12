import matplotlib . pyplot as plt


def next_node(r: float, s: float, R_i: list) -> float:
    return (r + s * R_i[-1] / (s + R_i[-1]))


def gen_data(r: float, s: float) -> list:
    R_i = [r + s]
    while len(R_i) < 2 or (R_i[-2] - R_i[-1] >= 1e-7):
        R_i.append(next_node(r, s, R_i))
    return R_i


if __name__ == "__main__":
    s = 10000.0
    r = 100.0
    R_i = gen_data(r=r, s=s)
    print(R_i[-1])
    plt.plot(R_i)
    plt.savefig("1_8.png")
