def sum_digits(n):
    return 0 if not n else 1 + ((n - 1) % 9)
    # while n >= 10:
    #     n = sum(int(a) for a in str(n))
    # return n

assert sum_digits(4523) == 5
assert sum_digits(65536) == 7
assert sum_digits(0) == 0
assert sum_digits(100) == 1
assert sum_digits(41) == 5
assert sum_digits(99) == 9
