def bar_triang(*args):
    return map(lambda a: round(sum(a) / 3.0, 4), zip(*args))

assert bar_triang([4, 6], [12, 4], [10, 10]), [8.6667, 6.6667]
assert bar_triang([4, 2], [12, 2], [6, 10]), [7.3333, 4.6667]
assert bar_triang([4, 8], [8, 2], [16, 6]), [9.3333, 5.3333]
