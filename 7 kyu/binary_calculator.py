BINARY = '{:b}'.format


def calculate(n1, n2, o):
    n1 = int(n1, 2)
    n2 = int(n2, 2)
    if o == 'add':
        return BINARY(n1 + n2)
    elif o == 'subtract':
        return BINARY(n1 - n2)
    return BINARY(n1 * n2)

assert calculate('1', '1', 'add') == '10'
assert calculate('1', '1', 'subtract') == '0'
assert calculate('1', '1', 'multiply') == '1'
