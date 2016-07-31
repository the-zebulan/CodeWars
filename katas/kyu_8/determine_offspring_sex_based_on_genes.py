def chromosoneCheck(sperm):
    """ chromosome_check == PEP8 (forced mixedCase by Codewars)
    Spelling mistake courtesy of Codewars as well
    """
    return "Congratulations! You're going to have a {}.".format(
        'son' if 'Y' in sperm else 'daughter'
    )
