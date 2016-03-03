def spread(func, args):
    return func(*args)

assert spread(lambda x, y: x + y, [1, 2]) == 3
# Equivalent: (lambda x,y: x+y)(1,2)
