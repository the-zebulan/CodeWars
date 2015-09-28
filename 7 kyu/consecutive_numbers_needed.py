def consecutive(arr):
    arr.sort()
    return len(set(xrange(arr[0], arr[-1] + 1)).difference(arr)) if arr else 0

assert consecutive([4, 8, 6]) == 2
assert consecutive([1, 2, 3, 4]) == 0
assert consecutive([]) == 0
assert consecutive([1]) == 0
assert consecutive([-10]) == 0
