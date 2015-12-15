VOWELS = frozenset('aeiouAEIOU')


def count_vowels(s=''):
    return sum(a in VOWELS for a in s) if isinstance(s, str) else None


assert count_vowels("abcdefg") == 2
assert count_vowels("asdfdsafdsafds") == 3
