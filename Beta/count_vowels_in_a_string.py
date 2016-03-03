VOWELS = frozenset('aeiouAEIOU')


def count_vowels(s=''):
    return sum(a in VOWELS for a in s) if isinstance(s, str) else None
