def sum_digits(n):
    return 0 if not n else 1 + ((n - 1) % 9)
    # while n >= 10:
    #     n = sum(int(a) for a in str(n))
    # return n
