from random import randint


def random_ints(n, total):
    result = []
    for _ in xrange(n - 1):
        num = randint(0, total)
        result.append(num)
        total -= num
    result.append(total)
    return result
