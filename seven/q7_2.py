import matplotlib.pyplot as plt


if __name__ == '__main__':
    x: list = [1/(i**2) for i in range(7, 100)]
    y: list = [[0.6032925128733665, 7], [0.6275177788944413, 12], [0.632302019211515, 17], [0.6341351594545814, 22]]
    y2: list = [0.48296421806607115, 0.49540056465742344, 0.49782997170379595, 0.49875299630324765]
#    plt.plot([i[1] for i in y], [i[0] for i in y])
#    plt.plot(range(len(x)), x)
    x1 = [1/(7**2), 1/(12**2), 1/(17**2), 1/(22**2)]
    y1 = [i[0] for i in y]
    grad = (y2[3] - y2[0]) / (x1[3] - x1[0])
#    plt.plot(x, [grad * i + 0.4999245680561941 for i in x])
    fig, ax = plt.subplots()
    AC, = ax.plot(x1, y1, marker='X', label='A to C')
    AB, = ax.plot(x1, y2, marker='X', label='A to B')
    ax.legend(handles=[AC, AB])
    fig.suptitle('Resistance with battery across A to C against $1/N^{2}$')
    ax.set_xlabel('Network size as $1/N^{2}$ where N is 2 greater than the actual network size')
    ax.set_ylabel('Resistance of network [$\Omega$]')
    plt.savefig('./q7_2_both.png')

