def reverse(n):
    exp = 1
    while n / 10 ** exp:
        exp += 1

    return sum((n % 10 ** a / 10 ** (a - 1)) * (10 ** b)
               for a, b in zip(xrange(1, exp + 1), xrange(exp - 1, -1, -1)))
