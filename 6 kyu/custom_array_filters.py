import __builtin__


class MyList(list):
    def __init__(self, iterable):
        """ Thanks to 'kurnos' from CodeWars """
        super(MyList, self).__init__(a for a in iterable if isinstance(a, int))

    def even(self):
        return filter(lambda b: b % 2 == 0, self)

    def in_range(self, low, hi):
        return filter(lambda c: low <= c <= hi, self)

    def odd(self):
        return filter(lambda d: d % 2 == 1, self)

    def over(self, limit):
        return filter(lambda e: e > limit, self)

    def under(self, limit):
        return filter(lambda f: f < limit, self)

__builtin__.list = MyList

assert list([1, 2, 3, 4, 5]).even() == [2, 4]
assert list([1, 2, 3, 4, 5]).odd() == [1, 3, 5]
assert list([1, 2, 3, 4, 5]).under(4) == [1, 2, 3]
assert list([1, 2, 3, 4, 5]).over(4) == [5]
assert list([1, 2, 3, 4, 5]).in_range(1, 3) == [1, 2, 3]
assert list(list([1,2,3,4,5,6,7,8,9,10]).even()).under(5) == [2, 4]
assert list(["a", 1, "b", 300, "x", "q", 63, 122, 181, "z", 0.83, 0.11]).even() == [300, 122]
