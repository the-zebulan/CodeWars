def pattern(n):
    return '\n'.join(str(a) * a for a in xrange(1, n + 1))
