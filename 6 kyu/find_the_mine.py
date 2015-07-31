def mineLocation(field):
    """ mine_location == PEP8, forced camelCase by CodeWars """
    for row, a in enumerate(field):
        for column, b in enumerate(a):
            if b == 1:
                return [row, column]

assert mineLocation([[1, 0], [0, 0]]) == [0, 0]
assert mineLocation([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == [0, 0]
assert mineLocation([[0, 0, 0, 0], [0, 0, 0, 0],
                     [0, 0, 1, 0], [0, 0, 0, 0]]) == [2, 2]
