def pattern(string):
    return '\n'.join(str(a) * a for a in xrange(2, string + 1, 2))
