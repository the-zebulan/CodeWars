from random import choice

UP_LOW = (str.upper, str.lower)


def random_case(strng):
    return ''.join(choice(UP_LOW)(a) for a in strng)
