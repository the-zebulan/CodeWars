def gimme(triplet):
    return triplet.index(sorted(triplet)[1])

assert gimme([2, 3, 1]) == 0
assert gimme([5, 10, 14]) == 1
