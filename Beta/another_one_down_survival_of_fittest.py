def remove_smallest(n, lst):
    if n <= 0:
        return lst
    elif n > len(lst):
        return []
    dex = [b[1] for b in sorted((a, i) for i, a in enumerate(lst))[:n]]
    return [c for i, c in enumerate(lst) if i not in dex]


assert remove_smallest((-10), [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert remove_smallest(0, [1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert remove_smallest(2, [5, 3, 2, 1, 4]) == [5, 3, 4]
assert remove_smallest(3, [5, 3, 2, 1, 4]) == [5, 4]
assert remove_smallest(3, [1, 2, 3, 4, 5]) == [4, 5]
assert remove_smallest(5, [1, 2, 3, 4, 5]) == []
assert remove_smallest(9, [1, 2, 3, 4, 5]) == []
assert remove_smallest(2, [1, 2, 1, 2, 1]) == [2, 2, 1]
