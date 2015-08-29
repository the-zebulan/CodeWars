def multiple(x):
    if x % 15 == 0:
        return 'BangBoom'
    elif x % 3 == 0:
        return 'Bang'
    elif x % 5 == 0:
        return 'Boom'
    return 'Miss'

assert multiple(30) == "BangBoom"
assert multiple(3) == "Bang"
assert multiple(98) == "Miss"
assert multiple(65) == "Boom"
assert multiple(23) == "Miss"
assert multiple(15) == "BangBoom"
