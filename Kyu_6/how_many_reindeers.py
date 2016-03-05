from math import ceil


def reindeer(presents):
    assert 0 <= presents <= 180
    return int(2 + (ceil(presents / 30.0)))
