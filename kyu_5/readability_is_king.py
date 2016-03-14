# Thanks to ChristianECooper's comments about the regex and findall problems
from itertools import groupby
from re import split

VOWELS = set('aeiouAEIOU')


def flesch_kincaid(text):
    sentences = syllables = words = 0.0
    for sentence in split(r'[!.]', text):
        if not sentence:
            break
        for word in sentence.split():
            syllables += sum(
                k for k, _ in groupby(1 if a in VOWELS else 0 for a in word))
            words += 1
        sentences += 1
    return round(
        0.39 * (words / sentences) + 11.8 * (syllables / words) - 15.59, 2)
