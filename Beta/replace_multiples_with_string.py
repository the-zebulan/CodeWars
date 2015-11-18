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


assert getNumber(0) == "BOTH"
assert getNumber(1) == 1
assert getNumber(2) == 2
assert getNumber(3) == "THREE"
assert getNumber(4) == 4
assert getNumber(5) == "FIVE"
assert getNumber(10) == "FIVE"
assert getNumber(15) == "BOTH"
assert getNumber(18) == "THREE"
assert getNumber(19) == 19
assert getNumber(30) == "BOTH"
assert getNumber(150) == "BOTH"
assert getNumber(-1) == -1
assert getNumber(-3) == "THREE"
assert getNumber(-15) == "BOTH"
assert getNumber(-50) == "FIVE"
assert getNumberRange(1, 15) == \
    [1, 2, "THREE", 4, "FIVE", "THREE", 7, 8, "THREE",
     "FIVE", 11, "THREE", 13, 14, "BOTH"]
assert getNumberRange(1, -15) == \
    [1, "BOTH", -1, -2, "THREE", -4, "FIVE", "THREE", -7,
     -8, "THREE", "FIVE", -11, "THREE", -13, -14, "BOTH"]
