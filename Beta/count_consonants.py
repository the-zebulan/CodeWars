VOWELS = set('aeiouAEIOU')


def consonant_count(s):
    return sum(1 for a in s if a.isalpha() and a not in VOWELS)


assert consonant_count('') == 0
assert consonant_count('aaaaa') == 0
assert consonant_count('Bbbbb') == 5
assert consonant_count('helLo world') == 7
assert consonant_count('h^$&^#$&^elLo world') == 7
