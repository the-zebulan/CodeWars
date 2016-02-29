def find_missing_numbers(arr):
    if not arr:
        return []
    return sorted(set(xrange(arr[0] + 1, arr[-1])).difference(arr))


assert find_missing_numbers([-3, -2, 1, 4]) == [-1, 0, 2, 3]
assert find_missing_numbers([-1, 0, 1, 2, 3, 4]) == []
assert find_missing_numbers([]) == []
assert find_missing_numbers([0]) == []
assert find_missing_numbers([-4, 4]) == [-3, -2, -1, 0, 1, 2, 3]
