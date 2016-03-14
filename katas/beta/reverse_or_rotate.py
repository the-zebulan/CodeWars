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
