def sum_mix(arr):
    result = 0
    for a in arr:
        try:
            result += a
        except TypeError:
            result += int(a)
    return result
