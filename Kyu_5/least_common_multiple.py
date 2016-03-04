# def lcm(*args):
#     """Compute the least common multiple of some non-negative integers"""
#     args = set(args)  # remove duplicates
#     if 0 in args:
#         return 0
#     x = max(args)
#     y = x
#     args.remove(x)
#     while any(x % z for z in args):
#         x += y
#     return x

from fractions import gcd


def lcm(*args):
    return reduce(lambda x, y: x * y / gcd(x, y), args)
