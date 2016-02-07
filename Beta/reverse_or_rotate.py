def revrot(digits, n):
    if not n:
        return ''
    result = []
    for a in xrange(0, len(digits) - n + 1, n):
        current = digits[a:a + n]
        if not sum(int(b) ** 3 for b in current) % 2:
            result.append(current[::-1])
        else:
            result.append('{0}{0}'.format(current)[1:n + 1])
    return ''.join(result)


assert revrot('123456987654', 6) == '234561876549'
assert revrot('123456987653', 6) == '234561356789'
assert revrot('66443875', 4) == '44668753'
assert revrot('66443875', 8) == '64438756'
assert revrot('664438769', 8) == '67834466'
assert revrot('123456779', 8) == '23456771'
assert revrot('', 8) == ''
assert revrot('123456779', 0) == ''
