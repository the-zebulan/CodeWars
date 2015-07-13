def pattern(n):
    nums = map(str, xrange(1, n + 1))
    return '\n'.join(''.join(nums[-a:]) for a in xrange(n, 0, -1))

assert pattern(1) == '1'
assert pattern(2) == '12\n2'
assert pattern(5) == '12345\n2345\n345\n45\n5'
assert pattern(10) == '12345678910\n2345678910\n345678910\n45678910\n' \
                      '5678910\n678910\n78910\n8910\n910\n10'
