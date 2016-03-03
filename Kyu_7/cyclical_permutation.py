def pattern(n):
    digits = map(str, xrange(1, n + 1))
    return '\n'.join(''.join(digits[b % n]
                             for b in xrange(a, a + n)) for a in xrange(n))

assert pattern(1) == '1'
assert pattern(4) == '1234\n2341\n3412\n4123'
assert pattern(10) == '12345678910\n23456789101\n34567891012\n45678910123\n' \
                      '56789101234\n67891012345\n78910123456\n89101234567\n' \
                      '91012345678\n10123456789'
