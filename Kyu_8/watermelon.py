def divide(weight):
    return weight % 2 == 0 and weight > 2

assert divide(4) is True
assert divide(88) is True
assert divide(2) is False
assert divide(67) is False
