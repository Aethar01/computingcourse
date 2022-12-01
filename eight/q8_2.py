from numpy import random, sqrt
from random import getrandbits
import neutrons


def neutron(L):
    loc = L * random.random()
    num = neutrons.neutrons()
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
    L = 0.1
    initfissions = 100
    avcount = 0
    while avcount < 100:
        temp = 0
        for i in range(1000):
            temp1 = 0
            for j in range(initfissions):
                temp1 += chain(*neutron(L), L=L)
            temp += temp1
        avcount = temp / 1000
        L += 0.001
    print(L)

#    count = 0
#    for i in range(initfissions):
#        count += chain(*neutron(L), L=L)
#    print(count)
