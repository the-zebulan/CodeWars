def multiples(s1, s2, s3):
    return [a for a in xrange(1, s3) if not(a % s1 or a % s2)]
