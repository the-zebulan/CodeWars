from collections import Counter


def find_it(seq):
    for k, v in Counter(seq).iteritems():
        if v % 2:
            return k


assert find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]) == 5
