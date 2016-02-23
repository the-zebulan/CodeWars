from random import shuffle


def rota(rooms):
    result = []
    for _ in xrange(0, 7, len(rooms)):
        shuffle(rooms)
        result.extend(rooms)
    return result[:7]
