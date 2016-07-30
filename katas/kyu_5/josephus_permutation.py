def josephus(items, k):
    dex = 0
    items_copy = list(items)
    result = []
    while items_copy:
        dex = (dex + (k - 1)) % len(items_copy)
        result.append(items_copy.pop(dex))
    return result
