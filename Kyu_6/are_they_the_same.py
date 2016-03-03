def comp(array1, array2):
    if None in (array1, array2):
        return False
    return sorted(a ** 2 for a in array1) == sorted(array2)

a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
assert comp(a1, a2) is True
assert comp([], None) is False
assert comp([], []) is True
