from itertools import groupby


def split_odd_and_even(n):
    return [int(''.join(str(b) for b in g)) for k, g in
            groupby((int(a) for a in str(n)), key=lambda b: b % 2)]
