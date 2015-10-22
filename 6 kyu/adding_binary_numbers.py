from itertools import izip_longest


def add(a, b):
    carry = '0'
    result = []
    for c, d in izip_longest(reversed(a), reversed(b), fillvalue='0'):
        w_carry = sum(e == '1' for e in (carry, c, d))
        result.append('0' if w_carry in (0, 2) else '1')
        carry = '0' if w_carry in (0, 1) else '1'
    result.append(carry)
    return ''.join(reversed(result)).lstrip('0') or '0'

assert add('111', '10') == '1001'
assert add('1101', '101') == '10010'
assert add('1101', '10111') == '100100'
assert add('10111', '001010101') == '1101100'
assert add('00', '0') == '0'
