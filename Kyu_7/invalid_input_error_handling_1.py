VOWELS = set('aeiouAEIOU')


def get_count(words=None):
    result = {'vowels': 0, 'consonants': 0}
    if not isinstance(words, str):
        return result
    for a in words:
        if a.isalpha():
            if a in VOWELS:
                result['vowels'] += 1
            else:
                result['consonants'] += 1
    return result
