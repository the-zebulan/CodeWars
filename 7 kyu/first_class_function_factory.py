def factory(x):
    return lambda b: map(lambda a: a * x, b)


my_arr = [1, 2, 3]

threes = factory(3)
assert threes(my_arr), [3, 6, 9]

fives = factory(5)
assert fives(my_arr), [5, 10, 15]
