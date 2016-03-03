def add(n):
    return lambda a: a + n

add_one = add(1)
assert add_one(3) == 4

add_three = add(3)
assert add_three(3) == 6
