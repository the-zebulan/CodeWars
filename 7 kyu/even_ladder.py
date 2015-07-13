pattern = lambda n: '\n'.join(str(a) * a for a in xrange(2, n + 1, 2))

assert pattern(8) == '22\n4444\n666666\n88888888'
assert pattern(5) == '22\n4444'
