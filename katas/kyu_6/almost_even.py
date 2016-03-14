def splitInteger(num, parts):
    """ split_integer == PEP8 (forced mixedCase by CodeWars) """
    quo, rem = divmod(num, parts)
    if rem == 0:
        return [quo] * parts
    return [quo if a > rem else quo + 1 for a in xrange(parts, 0, -1)]
