from random import random


def mutate(chromosome, p):
    return ''.join((a, '01'[a == '0'])[random() <= p] for a in chromosome)


zero = '0' * 100
one = '1' * 100

assert mutate(zero, 1) == one
assert mutate(one, 1) == zero

assert mutate(zero, 0) == zero
assert mutate(one, 0) == one
