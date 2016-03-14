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
