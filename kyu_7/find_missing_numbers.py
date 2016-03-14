def find_missing_numbers(arr):
    if not arr:
        return []
    return sorted(set(xrange(arr[0] + 1, arr[-1])).difference(arr))
