ROMAN = ((1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
         (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
         (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


def solution(n):
    result = []
    for num, char in ROMAN:
        q, n = divmod(n, num)
        result.append(q * char)
    return ''.join(result)


assert solution(1) == 'I'
assert solution(4) == 'IV'
assert solution(6) == 'VI'
