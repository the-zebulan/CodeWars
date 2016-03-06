from re import compile, match

REGEX = compile(r'(-[1-9]\d?|-1[0-1]\d|-12[0-8]|\d|[1-9]\d|1[0-1]\d|12[0-7])$')


def signed_eight_bit_number(number):
    m = match(REGEX, number)
    return bool(m) and m.group(0) == number
