def pattern(n):
    digits = map(str, xrange(1, n + 1))
    return '\n'.join(''.join(digits[b % n]
                             for b in xrange(a, a + n)) for a in xrange(n))
