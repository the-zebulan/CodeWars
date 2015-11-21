from fractions import gcd


def nbr_of_laps(x, y):
    lcm = (x * y) / gcd(x, y)
    return [lcm / x, lcm / y]


assert nbr_of_laps(5, 3) == [3, 5]
assert nbr_of_laps(4, 6) == [3, 2]
assert nbr_of_laps(5, 5) == [1, 1]
