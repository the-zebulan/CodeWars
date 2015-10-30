VOWELS = 'aeiou'


def getCount(string):
    """ get_count == PEP8 (forced mixedCase by CodeWars) """
    return sum(a in VOWELS for a in string.lower())

# getCount = lambda string: sum(a in VOWELS for a in string.lower())
assert getCount('abracadabra') == 5
