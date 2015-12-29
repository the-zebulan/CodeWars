VOWELS = 'aeiou'


def vowel_indices(word):
    return [i for i, a in enumerate(word.lower(), 1) if a in VOWELS]


assert vowel_indices("Mmmm") == []
assert vowel_indices("super") == [2, 4]
assert vowel_indices("Super") == [2, 4]
assert vowel_indices("Apple") == [1, 5]
