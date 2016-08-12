from itertools import groupby

VOWELS = frozenset('aeiou')


def trump_detector(trump_speech):
    total_extra_vowels = vowel_groups = 0.0
    for k, g in groupby(trump_speech.lower()):
        if k in VOWELS:
            vowel_groups += 1
            extra_vowels = sum(1 for _ in g) - 1
            if extra_vowels:
                total_extra_vowels += extra_vowels
    return round(total_extra_vowels / vowel_groups, 2)
