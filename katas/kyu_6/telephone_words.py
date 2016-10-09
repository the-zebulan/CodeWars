from itertools import product


def telephoneWords(s):
    """ telephone_words == PEP8 (forced mixedCase by Codewars) """
    letters = {'2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL',
               '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ'}
    return set(''.join(b) for b in product(*(letters.get(a, a) for a in s)))
