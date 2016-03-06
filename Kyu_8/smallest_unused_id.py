def next_id(arr):
    return min(set(xrange(max(arr) + 2)).difference(arr)) if arr else 0
