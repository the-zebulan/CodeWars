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


assert get_count(123) == 2
assert get_count(1230) == 5
assert get_count(1) == 0
assert get_count(1111111111) == 25
