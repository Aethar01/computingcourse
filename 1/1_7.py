from numpy import random


def gen_data(samples: int, _range: int) -> list:
    m: list = []
    for i in range(samples):
        n = random.normal() * _range
        m.append(n)
    return m


def countGreaterThan(data: list, min: float, max: float) -> float:
    count: int = 0
    for num in data:
        if not (min < num < max):
            count += 1
    return count


if __name__ == "__main__":
    samples = 1000000
    _range = 1
    repeats = 5
    count: float = sum([countGreaterThan(gen_data(samples, _range), -2, 2) for _x in range(repeats)]) / repeats
    print(f"{count / samples * 100}% are outside of the range -2 < x < 2")
