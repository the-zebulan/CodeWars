from string import maketrans


def decode(strng):
    return strng.translate(maketrans('1234567890', '9876043215'))


# def decode(strng):  # Python 3: no import necessary
#     return strng.translate(str.maketrans('1234567890', '9876043215'))
