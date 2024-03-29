from numpy import random, sqrt
from random import getrandbits
import neutrons
from math import sin, cos, acos, pi


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


if __name__ == '__main__':
    # initial value of L
    L = 0.1
    initfissions = 100
    # initialise average count
    avcount = 0
    # when the average count is larger than the initial number of fissions
    # there will be a greater number of secondary fissions vs initial ones
    # hence this is the critical value
    while avcount < initfissions:
        temp = 0
        for i in range(1000):
            temp1 = 0
            for j in range(initfissions):
                temp1 += chain(*neutron(L), L=L)
            temp += temp1
        avcount = temp / 1000
        L += 0.0001
    print(L)
