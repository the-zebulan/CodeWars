def getSlope(p1, p2):
    """ get_slope == PEP8 (forced mixedCase by CodeWars) """
    (x, y), (x2, y2) = p1, p2
    try:
        return (y - y2) / (x - x2)
    except ZeroDivisionError:
        pass
