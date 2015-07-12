def is_divisible(*args):
    n = args[0]
    return all(n % a == 0 for a in args[1:])

assert is_divisible(3, 3, 4) is False
assert is_divisible(12, 3, 4) is True
assert is_divisible(8, 3, 4, 2, 5) is False
