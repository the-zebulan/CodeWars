def unflatten(flat_array):
    dex = 0
    result = []
    while dex < len(flat_array):
        current = flat_array[dex]
        if current > 2:
            result.append(flat_array[dex:dex + current])
            dex += current
        else:
            result.append(current)
            dex += 1
    return result
