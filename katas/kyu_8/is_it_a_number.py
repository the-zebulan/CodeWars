def isDigit(strng):
    """ is_digit == PEP8 (forced mixedCase by Codewars) """
    try:
        float(strng)
        return True
    except ValueError:
        return False
