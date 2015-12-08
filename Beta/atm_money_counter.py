from re import compile, match

REGEX = compile(r'^(?:([a-zA-Z]+) ?(\d+)|(\d+) ?([a-zA-Z]+))$')
VALUES = {
    'USD': [1, 2, 5, 10, 20, 50, 100], 'CUP': [1, 3, 5, 10, 20, 50, 100],
    'RUB': [10, 50, 100, 500, 1000, 5000], 'UAH': [1, 2, 5, 10, 50, 100, 500],
    'SOS': [1000], 'EUR': [5, 10, 20, 50, 100, 200, 500]}


def atm(value):
    amount, currency = sorted(a for a in match(REGEX, value).groups() if a)
    currency = currency.upper()
    result = []
    try:
        denoms = VALUES[currency]
    except KeyError:
        return 'Sorry, have no {}.'.format(currency)
    rem = int(amount)
    for denom in reversed(denoms):
        quo, rem = divmod(rem, denom)
        if quo:
            result.append('{} * {} {}'.format(quo, denom, currency))
    if rem:
        return 'Can\'t do {} {}. Value must be divisible by {}!'\
            .format(amount, currency, denoms[0])
    return ', '.join(result)


assert atm('XSF 1000') == 'Sorry, have no XSF.'
assert atm('rub 12341') == 'Can\'t do 12341 RUB. Value must be divisible by 10!'
assert atm('10202UAH') == '20 * 500 UAH, 2 * 100 UAH, 1 * 2 UAH'
assert atm('842 usd') == '8 * 100 USD, 2 * 20 USD, 1 * 2 USD'
assert atm('euR1000') == '2 * 500 EUR'
assert atm('sos100') == 'Can\'t do 100 SOS. Value must be divisible by 1000!'
