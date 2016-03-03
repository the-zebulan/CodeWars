def square_sum(numbers):
    return sum(a ** 2 for a in numbers)

assert square_sum([1, 2]) == 5
assert square_sum([0, 3, 4, 5]) == 50
