def format_money(amount):
    return '${:.2f}'.format(amount)

assert format_money(39.99) == '$39.99'
