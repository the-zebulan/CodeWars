def square_digits(num):
    return int(''.join(str(int(a) ** 2) for a in str(num)))
