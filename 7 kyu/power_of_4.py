from math import log


def powerof4(n):
    if type(n) in (float, int) and n > 0:
        return log(n, 4).is_integer()
    return False


# def powerof4(n):
#     if n < 1 or isinstance(n, (bool, str)):
#         return False
#     while n > 1:
#         n /= 4.0
#         if int(n) != n:
#             return False
#     return True

assert powerof4(1024) is True
assert powerof4(102) is False
assert powerof4(64) is True
assert powerof4(1) is True
assert powerof4(25) is False
assert powerof4(-25) is False
assert powerof4('aa') is False
assert powerof4(True) is False
