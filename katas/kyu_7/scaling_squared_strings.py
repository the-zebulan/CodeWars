def scale(strng, k, n):
    return '\n'.join(''.join(b * k for b in a) for a in strng.split('\n')
                     for _ in xrange(n)) if strng else ''
