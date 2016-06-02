def compose(s1, s2):
    substrs = s1.split()
    n = len(substrs[0])
    return '\n'.join('{}{}'.format(a[:i], b[:n - (i - 1)]) for i, (a, b) in
                     enumerate(zip(substrs, reversed(s2.split())), 1))
