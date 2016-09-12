# coding=utf-8
UMLAUTS = {'A': 'Ä', 'E': 'Ë', 'I': 'Ï', 'O': 'Ö', 'U': 'Ü', 'Y': 'Ÿ',
           'a': 'ä', 'e': 'ë', 'i': 'ï', 'o': 'ö', 'u': 'ü', 'y': 'ÿ'}


def heavy_metal_umlauts(s):
    return ''.join(UMLAUTS.get(a, a) for a in s)
