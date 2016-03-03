from itertools import izip_longest


class Vector(object):
    def __init__(self, nums):
        self.nums = nums

    def __str__(self):
        return '({})'.format(','.join(str(a) for a in self.nums))

    def add(self, v2):
        return Vector([b + c for b, c in izip_longest(self.nums, v2.nums)])

    def dot(self, v2):
        return sum(d * e for d, e in izip_longest(self.nums, v2.nums))

    def equals(self, v2):
        return self.nums == v2.nums

    def norm(self):
        return sum(f ** 2 for f in self.nums) ** 0.5

    def subtract(self, v2):
        return Vector([g - h for g, h in izip_longest(self.nums, v2.nums)])


a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])
assert a.add(b).equals(Vector([4, 6, 8]))
assert a.subtract(b).equals(Vector([-2, -2, -2]))
assert a.dot(b) == 26
assert a.norm() == 14 ** 0.5
assert str(a) == '(1,2,3)'
try:
    assert a.add(c)  # different length lists raises an exception
except TypeError:
    print 'Vector list lengths MUST be the same!'

d = Vector([1, 2])
e = Vector([3, 4])
assert d.add(e).equals(Vector([4, 6]))
