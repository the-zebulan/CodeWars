def howManyLightsabersDoYouOwn(name='Luke'):
    """ how_many_lightsabers_do_you_own == PEP8
        (forced camelCase by codewars) """
    return 18 if name == 'Zach' else 0

assert howManyLightsabersDoYouOwn('Zach') == 18
assert howManyLightsabersDoYouOwn('Jim') == 0
