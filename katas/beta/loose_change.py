COINS = (
    (25, 'Quarters'),
    (10, 'Dimes'),
    (5, 'Nickels'),
    (1, 'Pennies')
)


def loose_change(cents):
    change = {'Pennies': 0, 'Nickels': 0, 'Dimes': 0, 'Quarters': 0}
    cents = int(cents)
    if cents <= 0:
        return change
    for coin_value, coin_name in COINS:
        q, r = divmod(cents, coin_value)
        change[coin_name] = q
        cents = r
    return change
