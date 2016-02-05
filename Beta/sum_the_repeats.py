def repeat_sum(lst):
    result = set()
    sets = [set(a) for a in lst]
    for i, b in enumerate(sets):
        for c in sets[i + 1:]:
            result.update(b & c)
    return sum(result)


assert repeat_sum([[1, 2, 3], [2, 8, 9], [7, 123, 8]]) == 10  # 2 + 8
assert repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]]) == 0
assert repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]]) == 9  # 1 + 8
