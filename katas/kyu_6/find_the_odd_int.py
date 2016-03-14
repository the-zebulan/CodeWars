from collections import Counter


def find_it(seq):
    for k, v in Counter(seq).iteritems():
        if v % 2:
            return k
