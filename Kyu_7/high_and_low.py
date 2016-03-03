def high_and_low(numbers):
    numbers = sorted(map(int, numbers.split()), reverse=True)
    return '{} {}'.format(numbers[0], numbers[-1])

assert high_and_low("1 2 3 4 5") == "5 1"
assert high_and_low("1 2 -3 4 5") == "5 -3"
assert high_and_low("1 9 3 4 -5") == "9 -5"
