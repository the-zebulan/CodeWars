def shorter_reverse_longer(a, b):
    if len(a) >= len(b):
        return '{0}{1}{0}'.format(b, a[::-1])
    return '{0}{1}{0}'.format(a, b[::-1])

assert shorter_reverse_longer("first", "abcde") == 'abcdetsrifabcde'
assert shorter_reverse_longer("hello", "bau") == 'bauollehbau'
assert shorter_reverse_longer("abcde", "fghi") == 'fghiedcbafghi'
