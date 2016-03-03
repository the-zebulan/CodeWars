def multiple(x):
    if x % 15 == 0:
        return 'BangBoom'
    elif x % 3 == 0:
        return 'Bang'
    elif x % 5 == 0:
        return 'Boom'
    return 'Miss'
