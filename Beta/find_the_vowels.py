VOWELS = set('aeiou')


def vowel_indices(word):
    return [i for i, a in enumerate(word.lower(), 1) if a in VOWELS]
