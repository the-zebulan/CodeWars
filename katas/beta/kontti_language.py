OUTPUT = 'ko{}-{}ntti'.format
VOWELS = frozenset('aeiouAEIOU')


def kontti(s):
    result = []
    for word in s.split():
        dex = next((i for i, a in enumerate(word) if a in VOWELS), -1) + 1
        result.append(OUTPUT(word[dex:], word[:dex]) if dex else word)
    return ' '.join(result)
