# coding=utf-8
table = {'A': 'α', 'B': 'β', 'D': 'δ', 'E': 'ε', 'I': 'ι', 'K': 'κ',
         'N': 'η', 'O': 'θ', 'P': 'ρ', 'R': 'π', 'T': 'τ', 'U': 'μ',
         'V': 'υ', 'W': 'ω', 'X': 'χ', 'Y': 'γ'}


def gr33k_l33t(string):
    result = []
    for a in string.upper():
        try:
            result.append(table[a])
        except KeyError:
            result.append(a.lower())
    return ''.join(result)
