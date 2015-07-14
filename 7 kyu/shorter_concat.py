def shorter_reverse_longer(a, b):
    if len(a) >= len(b):
        b, a = a, b
    return '{0}{1}{0}'.format(a, b[::-1])

assert shorter_reverse_longer("first", "abcde") == 'abcdetsrifabcde'
assert shorter_reverse_longer("hello", "bau") == 'bauollehbau'
assert shorter_reverse_longer("abcde", "fghi") == 'fghiedcbafghi'
