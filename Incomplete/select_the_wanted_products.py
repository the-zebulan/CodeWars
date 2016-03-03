from itertools import combinations
from math import cos, e, log, pi, sin, sqrt, tan


def prod_maker(lst, f):
    hmm = [round(a) for a in lst if isinstance(a, (float, int))]
    result = set()
    print lst
    print hmm
    for a in xrange(2, len(hmm) + 1):
        for b in combinations(hmm, a):
            current = reduce(lambda c, d: c * d, b)
            print b, current
            print f(current)
            print
            if f(current):
                result.add(current)
    return sorted(result)


# lst = []
# f = lambda x: x > 0
# print prod_maker(lst, f) == []
#
# lst = [3, -2, 2, 4, 5]
# f = lambda x: x >= 10
# print prod_maker(lst, f) == [10, 12, 15, 20, 24, 30, 40, 60, 120]
#
# lst = [3, -2, 2, 4, 5, 1]
# f = lambda x: - 20 < x < 80
# print prod_maker(lst, f) == [-16, -12, -10, -8, -6, -4, -2, 2, 3,
#                            4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60]
#
# lst = [3, -2, 2, 4, 5, 0.84,
#        2.07]  # it will be transformed to [3, -2, 2, 4, 5, 1, 2]
# f = lambda x: abs(x) > 35
# print prod_maker(lst, f) == [-480, -240, -160, -120, -96, -80,
#                            -60, -48, -40, 40, 48, 60, 80, 120, 240]
#
# lst = [3, -2, sqrt(2), log(20, e), tan(45 * pi / 180.0), cos(pi), sin(pi / 2.0)]
# f = lambda x: 10 <= abs(x) < 60 and x % 2 == 0
# print prod_maker(lst, f) == [-18, 18]

lst = ['', -1, pi, e, None, 'product', 0, log(60, 10)]
f = lambda x: x > 0 and x % 3 == 0
print prod_maker(lst, f)  # == [3, 6, 9, 18]
