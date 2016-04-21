from string import ascii_lowercase

AZ = dict(zip(ascii_lowercase, xrange(1, 27)))


def the_var(the_variables):
    return sum(AZ[a] for a in the_variables.split('+'))
