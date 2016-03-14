def same(arr_a, arr_b):
    return sorted(sorted(a) for a in arr_a) == sorted(sorted(b) for b in arr_b)
