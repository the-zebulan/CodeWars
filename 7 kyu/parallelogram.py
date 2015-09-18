from string import digits

OUTPUT = '{}{}{}'.format


def pattern(n):
    nums = ''.join(digits[a % 10] for a in xrange(1, n + 1))
    return '\n'.join(OUTPUT(' ' * (n - a), nums, ' ' * (a - 1)) for a in xrange(1, n + 1))

assert pattern(3) == "  123\n 123 \n123  "
assert pattern(5) == "    12345\n   12345 \n  12345  \n 12345   \n12345    "
assert pattern(8) == "       12345678\n      12345678 \n     12345678  \n    12345678   \n   12345678    \n  12345678     \n 12345678      \n12345678       "
