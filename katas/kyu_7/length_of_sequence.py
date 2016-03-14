def length_of_sequence(arr, n):
    total = [i for i, a in enumerate(arr) if a == n]
    return 0 if len(total) != 2 else total[1] - total[0] + 1
