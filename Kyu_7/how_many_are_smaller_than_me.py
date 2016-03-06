def smaller(arr):
    right_smaller = {}
    for dex_val in enumerate(arr):
        right_smaller.setdefault(dex_val, 0)
        val = dex_val[1]
        for key in right_smaller:
            if dex_val != key and val < key[1]:
                right_smaller[key] += 1
    return [right_smaller[b] for b in enumerate(arr)]
