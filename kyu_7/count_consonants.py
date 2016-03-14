VOWELS = set('aeiouAEIOU')


def consonant_count(s):
    return sum(1 for a in s if a.isalpha() and a not in VOWELS)
