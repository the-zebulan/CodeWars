def isOpposite(s1, s2):
    """ is_opposite == PEP8 (forced mixedCase by Codewars) """
    return False if not(s1 or s2) else s1.swapcase() == s2
