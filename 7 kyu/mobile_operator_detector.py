OPERATORS = {
    '039': 'Goldem Telecom', '050': 'MTS', '063': 'Life:)', '066': 'MTS',
    '067': 'Kyivstar', '068': 'Beeline', '093': 'Life:)', '095': 'MTS',
    '096': 'Kyivstar', '097': 'Kyivstar', '098': 'Kyivstar', '099': 'MTS'}


def detect_operator(num):
    return OPERATORS.get(str(num)[1:4], 'no info')


assert detect_operator(80661111841) == "MTS"
assert detect_operator(80671991111) == "Kyivstar"
assert detect_operator(80631551111) == "Life:)"
assert detect_operator(80931551111) == "Life:)"
assert detect_operator(80111551111) == "no info"
