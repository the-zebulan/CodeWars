# Thanks to ChristianECooper's comments about the regex and findall problems
from itertools import groupby
from re import findall, split

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


assert flesch_kincaid("The turtle is leaving.") == 3.67
assert flesch_kincaid("A good book is hard to find.") == -1.06
# # remember to use the average number of word BY SENTENCE; below: 2 sentences
assert flesch_kincaid("To be or not to be. That is the question.") == -0.66
assert flesch_kincaid('Do not cut your fingers as your katana is getting sharper! Be gentle.') == 4.19
assert flesch_kincaid(
    'Jumps hyperactive sweet sweet happy rests purrs jumps armchair? Sleeps '
    'sleeps food hyperactive cuddles armchair walks rests soft? Sleeps soft '
    'cover rests cat sun fun.') == 10.68
