def summation(x):
    return sum(xrange(1, x + 1)) if isinstance(x, int) else 'Error 404'

assert summation(10) == 55
assert summation(5) == 15
assert summation("538") == "Error 404"
assert summation(67.9) == "Error 404"
