def consecutive(arr):
    arr.sort()
    return len(set(xrange(arr[0], arr[-1] + 1)).difference(arr)) if arr else 0
