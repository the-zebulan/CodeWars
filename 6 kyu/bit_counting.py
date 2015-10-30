def countBits(n):
    """ count_bits == PEP8 (forced mixedCase by CodeWars) """
    return '{:b}'.format(n).count('1')

assert countBits(0) == 0
assert countBits(4) == 1
assert countBits(7) == 3
assert countBits(9) == 2
assert countBits(10) == 2
