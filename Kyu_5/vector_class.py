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
