def arrow(n):
    for i in xrange(n, 0, -1):
        print ''.join((''.join(str(j) for j in xrange(1, i)), str(i),
                       ''.join(str(j) for j in xrange(1, i))[::-1]))


arrow(5)
