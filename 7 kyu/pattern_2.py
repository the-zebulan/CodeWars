def pattern(n):
    nums = map(str, xrange(n, 0, -1))
    return '\n'.join(''.join(nums[:a]) for a in xrange(n, 0, -1))

assert pattern(1) == '1'
assert pattern(4) == '4321\n432\n43\n4'
assert pattern(5) == '54321\n5432\n543\n54\n5'
assert pattern(10) == '10987654321\n1098765432\n109876543\n10987654\n1098765\n109876\n10987\n1098\n109\n10'
