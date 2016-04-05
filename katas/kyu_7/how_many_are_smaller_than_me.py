def smaller(arr):
    return [sum(b < a for b in arr[i + 1:]) for i, a in enumerate(arr)]
