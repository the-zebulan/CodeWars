from numpy import multiply  # this works!

# def multiply(n, f):  # doesn't work (efficiently) for large numbers!
#     return sum(n for _ in xrange(f))


assert multiply(13, 7) == 91
