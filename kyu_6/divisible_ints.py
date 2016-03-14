def get_count(n):
    s = str(n)
    length = len(s)
    result = 0
    for a in xrange(1, length):
        for b in xrange(length - a + 1):
            try:
                if not n % int(s[b:b + a]):
                    result += 1
            except ZeroDivisionError:
                pass
    return result
