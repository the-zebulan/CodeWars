from random import random


def mutate(chromosome, p):
    return ''.join((a, '01'[a == '0'])[random() <= p] for a in chromosome)
