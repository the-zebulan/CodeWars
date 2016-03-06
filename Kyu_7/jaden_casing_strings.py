def toJadenCase(string):
    """ to_jaden_case == PEP8 (forced mixedCase by CodeWars) """
    return ' '.join(a.capitalize() for a in string.split())
