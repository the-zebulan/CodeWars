def smaller(arr):
    right_smaller = {}
    for dex_val in enumerate(arr):
        right_smaller.setdefault(dex_val, 0)
        val = dex_val[1]
        for key in right_smaller:
            if dex_val != key and val < key[1]:
                right_smaller[key] += 1
    return [right_smaller[b] for b in enumerate(arr)]


assert smaller([5, 4, 3, 2, 1]) == [4, 3, 2, 1, 0]
assert smaller([1, 2, 3]) == [0, 0, 0]
assert smaller([1, 2, 0]) == [1, 1, 0]
assert smaller([1, 2, 1]) == [0, 1, 0]
assert smaller([1, 1, -1, 0, 0]) == [3, 3, 0, 0, 0]
assert smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]) == [4, 1, 5, 5, 0, 0, 0, 0, 0]
