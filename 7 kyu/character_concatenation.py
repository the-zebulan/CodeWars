def char_concat(word):
    mid = len(word) / 2
    return ''.join('{}{}'.format(''.join(pair), i)
                   for i, pair in enumerate(zip(word[:mid],
                                                word[-mid:][::-1]), start=1))

assert char_concat("abcdef") == 'af1be2cd3'
assert char_concat("abc!def") == 'af1be2cd3'
