def create_iterator(func, n):
    def loop_it(a):
        for _ in xrange(n):
            a = func(a)
        return a
    return loop_it
