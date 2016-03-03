def order_weight(string):
    return ' '.join(c[1] for c in sorted((sum(int(b) for b in a), a)
                                         for a in string.split()))

assert order_weight('56 65 74 100 99 68 86 180 90') == \
    '100 180 90 56 65 74 68 86 99'
assert order_weight('103 123 4444 99 2000') == '2000 103 123 4444 99'
assert order_weight('2000 10003 1234000 44444444 9999 11 11 22 123') == \
    '11 11 2000 10003 22 123 1234000 44444444 9999'
