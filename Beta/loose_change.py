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


assert loose_change(56) \
    == {'Nickels': 1, 'Pennies': 1, 'Dimes': 0, 'Quarters': 2}
assert loose_change(-435) \
    == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
assert loose_change(4.935) \
    == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 0}
assert loose_change(29) \
    == {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters': 1}
assert loose_change(91) \
    == {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters': 3}
assert loose_change(0) \
    == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
assert loose_change(-2) \
    == {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters': 0}
assert loose_change(3.9) \
    == {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters': 0}
