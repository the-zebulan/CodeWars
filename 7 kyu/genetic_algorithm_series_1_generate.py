from random import choice

ONEZERO = '10'


def generate(length):
    return ''.join(choice(ONEZERO) for _ in xrange(length))


assert len(generate(16)) == 16
assert len(generate(32)) == 32
assert len(generate(64)) == 64
