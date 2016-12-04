def letter_pattern(words):
    return ''.join(a[0] if len(set(a)) == 1 else '*' for a in zip(*words))
