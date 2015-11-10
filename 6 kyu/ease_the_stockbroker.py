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


assert balance_statement(
    "ZNGA 1300 2.66 B, CLH15.NYM 50 56.32 B, OWW 1000 11.623 B, "
    "OGG 20 580.1 B") == "Buy: 29499 Sell: 0"

assert balance_statement('') == 'Buy: 0 Sell: 0'
assert balance_statement(
    'GOOG 300 542.0 B, AAPL 50 145.0 B, CSCO 250.0 29 B, GOOG 200 580.0 S') \
    == 'Buy: 169850 Sell: 116000; Badly formed 1: CSCO 250.0 29 B ;'
assert balance_statement(
    "CAP 1300 .2 B, CLH16.NYM 50 56 S, OWW 1000 11 S, OGG 20 580.1 S") \
    == 'Buy: 260 Sell: 11602; ' \
       'Badly formed 2: CLH16.NYM 50 56 S ;OWW 1000 11 S ;'
