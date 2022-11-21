from q5_4 import normalgen


if __name__ == '__main__':
    total: int = 9000000
    normaldist: list = normalgen(total)
    inrangecount: int = 0
    for x in normaldist:
        if x > -2.0 and x < 2.0:
            inrangecount += 1
        else:
            pass
    probinrange: float = inrangecount / len(normaldist)
    proboutofrange: float = 1 - probinrange
    print(f'Chance that x lies outside -2 < x < 2 is: {round(proboutofrange * 100, 4)}%')
