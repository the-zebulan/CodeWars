from itertools import groupby, izip_longest

ROMAN = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}


def solution(roman):
    pairs = [sum(g) for _, g in groupby(ROMAN[a] for a in roman)]
    return sum(a + b if a > b else b - a
               for a, b in izip_longest(pairs[::2], pairs[1::2], fillvalue=0))


assert solution('I') == 1
assert solution('IV') == 4
assert solution('XXI') == 21
assert solution('MMVIII') == 2008
assert solution('MDCLXVI') == 1666
