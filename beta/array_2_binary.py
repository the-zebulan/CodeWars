def arr2bin(arr):
    total = 0
    for a in arr:
        if not type(a) == int:
            return False
        total += a
    return '{:b}'.format(total)
