def where_is_he(p, bef, aft):
    return min(p - bef, aft + 1)

assert where_is_he(3, 1, 1) == 2
assert where_is_he(5, 2, 3) == 3
assert where_is_he(6, 5, 5) == 1
assert where_is_he(5, 4, 0) == 1
assert where_is_he(9, 4, 3) == 4
