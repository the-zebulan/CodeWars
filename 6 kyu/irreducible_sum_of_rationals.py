from fractions import Fraction


def sum_fracts(lst):
    answer = sum(Fraction(*a) for a in lst)
    numerator = answer.numerator
    denominator = answer.denominator
    if numerator == 0:
        return None
    elif denominator == 1:
        return numerator
    return [numerator, denominator]

assert sum_fracts([[1, 2], [1, 3], [1, 4]]) == [13, 12]
assert sum_fracts([[1, 3], [5, 3]]) == 2
