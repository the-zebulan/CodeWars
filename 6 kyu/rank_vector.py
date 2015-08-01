def ranks(array):
    ranking = {}
    for i, a in enumerate(sorted(array, reverse=True), start=1):
        if a not in ranking:
            ranking[a] = i
    return [ranking[b] for b in array]

assert ranks([]) == []
assert ranks([2]) == [1]
assert ranks([2, 2]) == [1, 1]
assert ranks([9, 3, 6, 10]) == [2, 4, 3, 1]
assert ranks([3, 3, 3, 3, 3, 5, 1]) == [2, 2, 2, 2, 2, 1, 7]
