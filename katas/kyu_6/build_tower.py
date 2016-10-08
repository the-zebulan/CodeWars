def tower_builder(n):
    length = n * 2 - 1
    return ['{:^{}}'.format('*' * a, length) for a in xrange(1, length + 1, 2)]
