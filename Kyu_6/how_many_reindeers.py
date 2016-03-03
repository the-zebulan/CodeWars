from math import ceil


def reindeer(presents):
    assert 0 <= presents <= 180
    return int(2 + (ceil(presents / 30.0)))


assert reindeer(0) == 2
assert reindeer(1) == 3
assert reindeer(30) == 3
try:
    reindeer(200)  # must throw an error
except AssertionError as e:
    print e
