from numpy import random


def generatedata(totalnums, bins):
    data = random.poisson()
    datarange = [x/bins for x in range(bins)]
    return data, datarange
