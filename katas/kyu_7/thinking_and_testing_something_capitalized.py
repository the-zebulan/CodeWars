def testit(s):
    return ' '.join(a.lower()[:-1] + a[-1].upper() for a in s.split())
