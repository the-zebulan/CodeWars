from operator import add, div, mul, sub


def basic_op(op, a, b):
    return {'+': add, '/': div, '*': mul, '-': sub}[op](a, b)
