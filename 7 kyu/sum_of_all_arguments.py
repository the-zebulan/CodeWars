sum_args = lambda *args: sum(args)

assert sum_args(1, 2, 3) == 6
assert sum_args(8, 2) == 10
assert sum_args(1, 2, 3, 4, 5) == 15
