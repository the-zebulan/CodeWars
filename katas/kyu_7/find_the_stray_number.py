def stray(arr):
    return reduce(lambda prev, curr: prev ^ curr, arr)
