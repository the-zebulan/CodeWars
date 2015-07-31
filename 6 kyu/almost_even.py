def splitInteger(num, parts):
    """ split_integer == PEP8, forced camelCase by CodeWars """
    quo, rem = divmod(num, parts)
    if rem == 0:
        return [quo] * parts
    return [quo if a > rem else quo + 1 for a in range(parts, 0, -1)]

assert splitInteger(20, 6) == [3, 3, 3, 3, 4, 4]
assert splitInteger(10, 1) == [10]
assert splitInteger(2, 2) == [1, 1]
assert splitInteger(20, 5) == [4, 4, 4, 4, 4]
