from collections import Counter


def anagrams(word, words):
    word_cnt = Counter(word)
    return [a for a in words if Counter(a) == word_cnt]


assert anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) == ['aabb', 'bbaa']
assert anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) \
    == ['carer', 'racer']
assert anagrams('laser', ['lazing', 'lazy',  'lacer']) == []
