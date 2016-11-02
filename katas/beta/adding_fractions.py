from fractions import Fraction


def add_fracs(*args):
    return str(sum(Fraction(a) for a in args)) if args else ''
