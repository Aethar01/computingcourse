from numpy import zeros, random


def randbin(totalrandnumbers, numofbins):
    m = zeros(numofbins, int)
    for i in range(totalrandnumbers):
        n = random.randint(numofbins)
        m[n] = m[n]+1
    return m


def randbin1(totalrandomnumbers, totalbins, average=1):
    m = zeros(totalbins, int)
    for i in range(totalrandomnumbers):
        n = sum([random.random() for x in range(average)]) / average
        k = int(totalbins*n)
        m[k] = m[k] + 1
    return m


if __name__ == '__main__':
    print(randbin(1000, 10))
