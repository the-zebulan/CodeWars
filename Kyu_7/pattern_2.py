def pattern(n):
    nums = map(str, xrange(n, 0, -1))
    return '\n'.join(''.join(nums[:a]) for a in xrange(n, 0, -1))
