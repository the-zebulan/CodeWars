from itertools import izip

VALUES = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def convert_num(n):
    return sum(10 ** c * VALUES[d] for c, d in
               izip(xrange(len(n) - 1, -1, -1), n))


def multiplyMyNumbers(a, b):
    """ multiply_my_numbers == PEP8 (forced mixedCase by CodeWars) """
    return str(convert_num(a) * convert_num(b))
