from random import choice

ONEZERO = '10'


def generate(length):
    return ''.join(choice(ONEZERO) for _ in xrange(length))
