def openOrSenior(data):
    """ open_or_senior == PEP8 """
    return ['Senior' if age >= 55 and h > 7 else 'Open' for age, h in data]

assert openOrSenior([[45, 12], [55, 21], [19, -2], [104, 20]]) == \
    ['Open', 'Senior', 'Open', 'Senior']
assert openOrSenior([[16, 23], [73, 1], [56, 20], [1, -1]]) == \
    ['Open', 'Open', 'Senior', 'Open']
