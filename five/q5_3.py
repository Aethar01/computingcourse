from q5_1 import randbin
import matplotlib.pyplot as plt

if __name__ == '__main__':
    total = 1000
    maximumint = 10
    plt.bar(range(maximumint), randbin(total, maximumint), width=1, align='edge')
    plt.xticks(range(maximumint + 1))
    plt.savefig('./q5_3.png')

