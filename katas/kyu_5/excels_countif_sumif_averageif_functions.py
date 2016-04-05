from operator import eq, ge, gt, le, lt, ne
import re

OPERATORS = {'>=': ge, '>': gt, '<=': le, '<': lt, '<>': ne}
REGEX = re.compile(r'(\d+\.\d+|\d+)')


def average_if(values, criteria):
    func = get_func(criteria)
    total_values = values_sum = 0.0
    for a in values:
        if func(a):
            total_values += 1
            values_sum += a
    return values_sum / total_values


def count_if(values, criteria):
    func = get_func(criteria)
    return sum(func(b) for b in values)


def get_func(criteria):
    try:
        op, num, _ = REGEX.split(criteria)
        return lambda c: OPERATORS[op](c, float(num))
    except (TypeError, ValueError):
        return lambda d: eq(d, criteria)


def sum_if(values, criteria):
    func = get_func(criteria)
    return sum(e for e in values if func(e))
