from itertools import product


def phonewords(digits):
    letters = {'2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL', '6': 'MNO',
               '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'}
    return [''.join(a) for a in product(*(letters.get(b, b) for b in digits))]
