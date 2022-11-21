import matplotlib.pyplot as plt
from q5_4 import randbin

if __name__ == '__main__':
    total = 1000
    maximumint = 10
    plt.bar(range(maximumint), randbin(total, maximumint), width=1, align='edge')
    plt.xticks(range(maximumint + 1))
    plt.xlabel('Random number value')
    plt.ylabel('Frequency Density')
    plt.savefig('./q5_3.png')

