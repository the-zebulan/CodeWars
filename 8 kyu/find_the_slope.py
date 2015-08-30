def find_slope(points):
    x, y, x2, y2 = points
    try:
        return str((y2 - y) / (x2 - x))
    except ZeroDivisionError:
        return 'undefined'

assert find_slope([19, 3, 20, 3]) == '0'
assert find_slope([-7, 2, -7, 4]) == 'undefined'
assert find_slope([10, 50, 30, 150]) == '5'
assert find_slope([10, 20, 20, 80]) == '6'
assert find_slope([-10, 6, -10, 3]) == 'undefined'
