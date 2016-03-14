def getNumber(number):
    if not number % 15:
        return 'BOTH'
    elif not number % 5:
        return 'FIVE'
    elif not number % 3:
        return 'THREE'
    return number


def getNumberRange(first, last):
    step = 1 if first < last else -1
    return map(getNumber, xrange(first, last + step, step))
    # return [getNumber(a) for a in xrange(first, last + step, step)]
