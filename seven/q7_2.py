import matplotlib.pyplot as plt


if __name__ == '__main__':
    x: list = [1/(i**2) for i in range(7, 100)]
    y: list = [[0.6032925128733665, 7], [0.6275177788944413, 12], [0.632302019211515, 17], [0.6341351594545814, 22]]
#    plt.plot([i[1] for i in y], [i[0] for i in y])
#    plt.plot(range(len(x)), x)
    x1 = [1/(7**2), 1/(12**2), 1/(17**2), 1/(22**2)]
    y1 = [i[0] for i in y]
    grad = (y1[3] - y1[0]) / (x1[3] - x1[0])
    plt.plot(x, [grad * i + 0.6364830719829574 for i in x])
    plt.plot(x1, y1, marker='X')

    plt.savefig('./q7_2.png')

