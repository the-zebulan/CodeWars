from itertools import groupby, izip_longest

FROM_ROMAN = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
TO_ROMAN = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


class RomanNumerals(object):
    @staticmethod
    def to_roman(n):
        result = []
        for num, char in TO_ROMAN:
            q, n = divmod(n, num)
            result.append(q * char)
        return ''.join(result)

    @staticmethod
    def from_roman(roman):
        pairs = [sum(g) for _, g in groupby(FROM_ROMAN[a] for a in roman)]
        return sum(a + b if a > b else b - a for a, b in
                   izip_longest(pairs[::2], pairs[1::2], fillvalue=0))
