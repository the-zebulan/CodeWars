TO_ROMAN = (
    (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'),
    (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I'))


def arabic_to_roman(arabic):
    if not 0 < arabic < 1000:
        return 'NaR'
    result = []
    for num, char in TO_ROMAN:
        q, arabic = divmod(arabic, num)
        result.append(q * char)
    return ''.join(result)


assert arabic_to_roman(-1) == "NaR"
assert arabic_to_roman(0) == "NaR"
assert arabic_to_roman(1000) == "NaR"
assert arabic_to_roman(1) == "I"
assert arabic_to_roman(2) == "II"
assert arabic_to_roman(3) == "III"
assert arabic_to_roman(4) == "IV"
assert arabic_to_roman(5) == "V"
assert arabic_to_roman(6) == "VI"
assert arabic_to_roman(599) == "DXCIX"
