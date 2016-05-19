from random import randint, random


def throw_rigged():
    if random() < 0.22:
        return 6
    return randint(1, 5)
