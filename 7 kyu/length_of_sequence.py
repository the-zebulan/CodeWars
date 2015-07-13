def length_of_sequence(arr, n):
    total = [i for i, a in enumerate(arr) if a == n]
    return 0 if len(total) != 2 else total[1] - total[0] + 1

assert length_of_sequence([1, 1], 1) == 2
assert length_of_sequence([1, 2, 3, 1], 1) == 4
assert length_of_sequence([-7, 5, 0, 2, 9, 5], 10) == 0
assert length_of_sequence([-7, 5, 0, 2, 9, 5], 5) == 5
assert length_of_sequence([1, 2, 3, 1, 2, 3, 1], 1) == 0
