def transpose(arr):
    return map(list, zip(*arr)) if all(arr) else [[]]
