from itertools import permutations as perm


def permutations(strng):
    return set(''.join(a) for a in perm(strng))


assert sorted(permutations('a')) == ['a']
assert sorted(permutations('ab')) == ['ab', 'ba']
assert sorted(permutations('aabb')) \
    == ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
