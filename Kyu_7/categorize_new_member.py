def openOrSenior(data):
    """ open_or_senior == PEP8 (forced mixedCase by CodeWars) """
    return ['Senior' if age >= 55 and h > 7 else 'Open' for age, h in data]
