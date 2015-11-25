from itertools import permutations


def get_words(hash_of_letters):
    return sorted(''.join(b) for b in set(permutations(''.join(
        k * a for k, v in hash_of_letters.iteritems() for a in v))))


assert get_words({1: ['a', 'b', 'c']}) \
    == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
assert get_words({2: ['a'], 1: ['b', 'c']}) \
    == ['aabc', 'aacb', 'abac', 'abca', 'acab', 'acba',
        'baac', 'baca', 'bcaa', 'caab', 'caba', 'cbaa']
