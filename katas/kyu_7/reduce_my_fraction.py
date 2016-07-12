from fractions import Fraction


def reduce(fraction):
    """ Shadows built-in name 'reduce' (forced by Codewars) """
    f = Fraction(*fraction)
    return [f.numerator, f.denominator]
