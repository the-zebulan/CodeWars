def count(lst):
    return sum(1 for _ in lst)

assert count([1, 2, 3, 4]) == 4
