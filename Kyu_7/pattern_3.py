def pattern(n):
    nums = map(str, xrange(n, 0, -1))
    return '\n'.join(''.join(nums[:a]) for a in xrange(1, n + 1))

assert pattern(1) == '1'
assert pattern(2) == '2\n21'
assert pattern(5) == '5\n54\n543\n5432\n54321'
