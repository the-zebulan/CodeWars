# def is_square(n):
#     if n < 1:
#         return False
#     sqrt = n ** 0.5
#     return sqrt == int(sqrt)


def is_square(n):
    return n > 0 and (n ** 0.5).is_integer()
