from re import compile, match

BUY_SELL = 'Buy: {:.0f} Sell: {:.0f}'.format
REGEX = compile(r'\S+ (?P<qty>\d+) (?P<price>\d*\.\d+) (?P<status>[BS])$')


def balance_statement(lst):
    if not lst:
        return BUY_SELL(0, 0)
    badly_formed = []
    buy = mistakes = sell = 0
    for order in lst.split(', '):
        check = match(REGEX, order)
        if check:
            total = int(check.group('qty')) * float(check.group('price'))
            if check.group('status') == 'B':
                buy += total
            else:
                sell += total
        else:
            badly_formed.append('{} ;'.format(order))
            mistakes += 1
    if not badly_formed:
        return BUY_SELL(buy, sell)
    return '{}; Badly formed {}: {}'.format(
        BUY_SELL(buy, sell), mistakes, ''.join(badly_formed))
