# VOWELS = 'aeiou'
#
#
# def disemvowel(string):
#     return ''.join(a for a in string if not a.lower() in VOWELS)


def disemvowel(s):
    return s.translate(None, 'aeiouAEIOU')
