from functools import partial


class Foo(object):
    def __init__(self):
        self.func = int
        self.arr_of_funcs = [partial(int, base=2), partial(int, base=8)]

    def convert(self, num, base):
        return self.arr_of_funcs[base](num)
