def create_iterator(func, n):
    def loop_it(a):
        for _ in xrange(n):
            a = func(a)
        return a
    return loop_it


# test function, not part of solution
def get_double(n):
    return n * 2


double_iterator = create_iterator(get_double, 1)
assert double_iterator(3) == 6
assert double_iterator(5) == 10

get_quadruple = create_iterator(get_double, 2)
assert get_quadruple(2) == 8
assert get_quadruple(5) == 20
