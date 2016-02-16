from re import compile, sub

REGEX = compile(r',+')


def dad_filter(strng):
    return sub(REGEX, ',', strng).rstrip(' ,')


assert dad_filter('all this,,,, used to be trees,,,,,,') == \
    'all this, used to be trees'
assert dad_filter('Listen,,,, kid,,,,,,') == 'Listen, kid'
assert dad_filter('Luke,,,,,,,,, I am your father,,,,,,,,,  ') == \
    'Luke, I am your father'
assert dad_filter(
    'i,, don\'t believe this round earth,,, show me evadence!!') == \
    'i, don\'t believe this round earth, show me evadence!!'
assert dad_filter('Dead or alive,,,, you\'re coming with me,,,   ') == \
    'Dead or alive, you\'re coming with me'
