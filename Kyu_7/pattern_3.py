def pattern(n):
    nums = map(str, xrange(n, 0, -1))
    return '\n'.join(''.join(nums[:a]) for a in xrange(1, n + 1))
