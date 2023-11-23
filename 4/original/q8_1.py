from numpy import random, sqrt
from random import getrandbits


def neutron(L):
    loc = L * random.random()
    num = 2
    return (loc, num)


def chain(loc, num, L):
    R = sqrt(2 * 0.017 * 0.21)
    newloc = []
    temp = []
    for i in range(num):
        direc = bool(getrandbits(1))
        if direc:
            newloc.append(loc + R)
        else:
            newloc.append(loc - R)
    for i in range(len(newloc)):
        if newloc[i] < L and newloc[i] > 0:
            pass
        else:
            temp.append(newloc[i])
    for i in temp:
        del newloc[newloc.index(i)]
    return len(newloc)


if __name__ == '__main__':
    L = 1
    sims = 100
    count = 0
    for i in range(sims):
        count += chain(*neutron(L), L=L)
    print(count)
