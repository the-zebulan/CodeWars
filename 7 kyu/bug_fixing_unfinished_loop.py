def create_array(n):
    return range(1, n + 1)


# def create_array(n):
#     res = []
#     i = 1
#     while i <= n:
#         res+=[i]
#         i += 1
#     return res

assert create_array(1), [1]
assert create_array(2), [1, 2]
assert create_array(3), [1, 2, 3]
assert create_array(4), [1, 2, 3, 4]
assert create_array(5), [1, 2, 3, 4, 5]
