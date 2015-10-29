from collections import Counter


class List(object):
    @staticmethod
    def count_spec_digits(integers_list, digits_list):
        counts = Counter(''.join(str(abs(a)) for a in integers_list))
        return [(b, counts[str(b)]) for b in digits_list]

l = List()

integers_list = [1, 1, 2, 3, 1, 2, 3, 4]
digits_list = [1, 3]
assert l.count_spec_digits(integers_list, digits_list) == [(1, 3), (3, 2)]

integers_list = [-18, -31, 81, -19, 111, -888]
digits_list = [1, 8, 4]
assert l.count_spec_digits(integers_list, digits_list) == \
    [(1, 7), (8, 5), (4, 0)]

integers_list = [-77, -65, 56, -79, 6666, 222]
digits_list = [1, 8, 4]
assert l.count_spec_digits(integers_list, digits_list) == \
    [(1, 0), (8, 0), (4, 0)]

integers_list = []
digits_list = [1, 8, 4]
assert l.count_spec_digits(integers_list, digits_list) == \
    [(1, 0), (8, 0), (4, 0)]
