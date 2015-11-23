def sum_all(*args):
    try:
        return sum(args)
    except TypeError:
        return False


assert sum_all(6, 2, 3) == 11
assert sum_all(756, 2, 1, 10) == 769
assert sum_all(76856, -32, 1981, 1076) == 79881
assert sum_all(1, -32, "codewars", 1076) is False
assert sum_all(7, -3452, 1981, 1076) == -388
