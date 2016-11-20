def arr_check(arr):
    return all(isinstance(a, list) for a in arr)
