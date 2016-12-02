from itertools import groupby


def group_ints(lst, key=0):
    return [list(g) for _, g in groupby(lst, lambda a: a < key)]


# PEP8: katas function name should use snake_case
groupInts = group_ints
