def mineLocation(field):
    """ mine_location == PEP8 (forced mixedCase by CodeWars) """
    for row, a in enumerate(field):
        for column, b in enumerate(a):
            if b == 1:
                return [row, column]
