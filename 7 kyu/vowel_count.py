VOWELS = 'aeiou'


def getCount(string):
    return sum(a in VOWELS for a in string.lower())

# getCount = lambda string: sum(a in VOWELS for a in string.lower())
assert getCount('abracadabra') == 5
