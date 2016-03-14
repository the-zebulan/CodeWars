def high_and_low(numbers):
    numbers = sorted(map(int, numbers.split()), reverse=True)
    return '{} {}'.format(numbers[0], numbers[-1])
