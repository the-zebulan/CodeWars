def maskify(cc):
    return '{:#>{}}'.format(cc[-4:], len(cc))

assert maskify('4556364607935616') == '############5616'
assert maskify('64607935616') == '#######5616'
assert maskify('1') == '1'
assert maskify('') == ''
