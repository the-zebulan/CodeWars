def getSubstrings(s):
    """ get_substrings == PEP8 (forced mixedCase by CodeWars) """
    s = s.lower()
    length = len(s)
    seen = set()
    for a in xrange(length):
        for b in xrange(1, length + 1):
            end = a + b
            if end > length:
                break
            seen.add(s[a:end])
    return len(seen)


assert getSubstrings('YOLO') == 9
assert getSubstrings('I am but a string in the meadow.') == 511
