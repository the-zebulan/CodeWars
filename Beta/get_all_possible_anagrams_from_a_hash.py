from itertools import permutations


def get_words(hash_of_letters):
    return sorted(''.join(b) for b in set(permutations(''.join(
        k * a for k, v in hash_of_letters.iteritems() for a in v))))
