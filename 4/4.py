from numpy import random, sqrt
from random import getrandbits
import neutrons
from math import sin, cos, acos, pi
from multiprocessing import Pool


def one():
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

    L = 1
    sims = 100
    count = 0
    for i in range(sims):
        count += chain(*neutron(L), L=L)
    print(f"Over 100 simulations {count} neutrons stay in the rod length L")


def two():
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
    print(f"Critical value in a one dimensional rod is {L}")


def neutron(L):
    # array of random coords from 0 to L
    loc = [L * random.random(), L * random.random(), L * random.random()]
    # random number with average of 2
    num = neutrons.neutrons()
    return (loc, num)


def chain(loc, num, L):
    R = sqrt(2 * 0.017 * 0.21)
    newloc = []
    temp = []
    for i in range(num):
        # generate random direction vector
        direc = [R * neutrons.diffusion() * sin(acos(2.0 * random.random() - 1.0)) * cos(2.0 * pi * random.random()),
                 R * neutrons.diffusion() * sin(acos(2.0 * random.random() - 1.0)) * sin(2.0 * pi * random.random()),
                 R * neutrons.diffusion() * cos(acos(2.0 * random.random() - 1.0))]
        # add random vector to the original location
        newloc.append([direc[i] + loc[i] for i in range(len(loc))])
    # if any of the locations of neutrons are outside of the cube, delete them from the array
    for i in range(len(newloc)):
        if newloc[i][0] < L and newloc[i][0] > 0 and newloc[i][1] < L and newloc[i][1] > 0 \
                and newloc[i][2] < L and newloc[i][2] > 0:
            pass
        else:
            temp.append(newloc[i])
    for i in temp:
        del newloc[newloc.index(i)]
    # return a count of how many neutrons are still in the cube (hence generate new fission reactions)
    return len(newloc)


def sampled(L, initfissions=100):
    temp = 0
    for i in range(1000):
        temp1 = 0
        for j in range(initfissions):
            temp1 += chain(*neutron(L), L=L)
        temp += temp1
    return (temp / 1000, L)


def four():
    L = 0.1
    initfissions = 100
    p = Pool()
    temp = p.map(sampled, [L + 0.001 * i for i in range(200)])
    p.close()
    closest = min(temp, key=lambda x: abs(x[0] - initfissions))
    print(f"Critical value in a three dimensional cube is {closest[1]} with {closest[0]} neutrons")
    return temp


def graph4(temp):
    import matplotlib.pyplot as plt
    plt.plot([temp[i][1] for i in range(len(temp))], [temp[i][0] for i in range(len(temp))])
    plt.xlabel("Length of cube faces [m]")
    plt.ylabel("Number of neutrons in cube bounds from 100 fissions")
    plt.title("Critical value in a three dimensional cube")
    plt.savefig("./4_50.png")


if __name__ == "__main__":
    one()
    two()
    fourdata = four()
    graph4(fourdata)
