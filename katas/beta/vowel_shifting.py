def vowel_shift(text, n):
    if not text:
        return text
    non_vowels = []
    only_vowels = []
    vowels = set('aeiouAEIOU')
    for a in text:
        if a in vowels:
            only_vowels.append(a)
            non_vowels.append('{}')
        else:
            non_vowels.append(a)
    if not only_vowels:
        return text
    mod = n % len(only_vowels)
    return ''.join(non_vowels).format(*only_vowels[-mod:] + only_vowels[:-mod])
