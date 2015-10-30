def to_currency(price):
    return '{:,}'.format(price)


assert to_currency(123456) == "123,456"
assert to_currency(1234) == "1,234"
assert to_currency(123) == "123"
assert to_currency(123456789012) == "123,456,789,012"
