def string_suffix(string):
    total = 0
    for a in xrange(len(string)):
        for b, c in zip(string, string[a:]):
            if not b == c:
                break
            total += 1
    return total
