def char_concat(word):
    mid = len(word) / 2
    return ''.join('{}{}'.format(''.join(pair), i)
                   for i, pair in enumerate(zip(word[:mid],
                                                word[-mid:][::-1]), start=1))
