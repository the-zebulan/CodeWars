def copy_list(l):
    return l[:]

t = [1, 2, 3, 4]
t_copy = copy_list(t)
t[1] += 5
assert t == [1, 7, 3, 4]
assert t_copy == [1, 2, 3, 4]
