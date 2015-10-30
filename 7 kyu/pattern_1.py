def pattern(n):
    return '\n'.join(str(a) * a for a in xrange(1, n + 1))

assert pattern(1) == '1'
assert pattern(2) == '1\n22'
assert pattern(5) == '1\n22\n333\n4444\n55555'
