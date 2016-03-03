def next_id(arr):
    return min(set(xrange(max(arr) + 2)).difference(arr)) if arr else 0

assert next_id([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11
assert next_id([5, 4, 3, 2, 1]) == 0
assert next_id([0, 1, 2, 3, 5]) == 4
assert next_id([0, 0, 0, 0, 0, 0]) == 1
assert next_id([]) == 0
