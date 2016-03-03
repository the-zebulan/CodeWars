OUTPUT = '1{}{}'.format


def pattern(n):
    return '\n'.join(OUTPUT('*' * a, a + 1 if a else '') for a in xrange(n))
