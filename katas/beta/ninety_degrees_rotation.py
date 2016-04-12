def rotate(arr):
    return [list(a) for a in zip(*reversed(arr))]
