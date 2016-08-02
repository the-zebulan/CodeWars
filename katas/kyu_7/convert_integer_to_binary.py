def to_binary(n):
    return '{:b}'.format(n & 4294967295)
    # return '{:b}'.format(n & 0xffffffff)
    # return '{:b}'.format(n & 0b11111111111111111111111111111111)
