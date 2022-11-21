from numpy import random


def generatedata(totalnums: int, mean: int):
    data = random.poisson(mean, totalnums)
    return data


if __name__ == '__main__':
    poissondist = generatedata(100000, 15)
    datamean = sum(poissondist) / len(poissondist)
    print(f'The average of 100000 counts of random.poisson with a mean of 15 is {datamean}')
