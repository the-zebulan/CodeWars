def find_even_index(*lst):
    left_sum = 0
    right_sum = sum(lst[0])
    for i, a in enumerate(lst[0]):
        right_sum -= a
        if left_sum == right_sum:
            return i
        left_sum += a
    return -1


assert find_even_index([1, 2, 3, 4, 3, 2, 1]) == 3
assert find_even_index([1, 100, 50, -51, 1, 1]) == 1
assert find_even_index([1, 2, 3, 4, 5, 6]) == -1
assert find_even_index([20, 10, 30, 10, 10, 15, 35]) == 3
assert find_even_index([20, 10, -80, 10, 10, 15, 35]) == 0
assert find_even_index([10, -80, 10, 10, 15, 35, 20]) == 6
assert find_even_index(range(1, 100)) == -1
assert find_even_index([0, 0, 0, 0, 0]) == 0
assert find_even_index([-1, -2, -3, -4, -3, -2, -1]) == 3
assert find_even_index(range(-100, -1)) == -1
