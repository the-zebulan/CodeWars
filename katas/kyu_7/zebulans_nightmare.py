def zebulansNightmare(strng):
    """ zebulans_nightmare == PEP8 (forced mixedCase by CodeWars) """
    words = strng.split('_')
    return '{}{}'.format(words[0], ''.join(a.capitalize() for a in words[1:]))
