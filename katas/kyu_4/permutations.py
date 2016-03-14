from itertools import permutations as perm


def permutations(strng):
    return set(''.join(a) for a in perm(strng))
