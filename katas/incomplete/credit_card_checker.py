def valid_card(card_number):
    total = 0
    for i, a in enumerate(reversed(card_number.replace(' ', ''))):
        if i % 2:
            current = int(a) * 2
            total += current - 9 if current > 8 else current
        else:
            total += int(a)
    return not total % 10


print valid_card('5457 6238 9823 4311') # -> true
print valid_card('5457 6238 9323 4311') # -> false

assert valid_card('5457 6238 9823 4311') is True
assert valid_card('8895 6238 9323 4311') is False
assert valid_card('5457 6238 5568 4311') is False
assert valid_card('5457 6238 9323 4311') is False
assert valid_card('2222 2222 2222 2224') is True
assert valid_card('5457 1125 9323 4311') is False
assert valid_card('1252 6238 9323 4311') is False
assert valid_card('9999 9999 9999 9995') is True
assert valid_card('0000 0300 0000 0000') is False
assert valid_card('4444 4444 4444 4448') is True
assert valid_card('5457 6238 9323 1252') is False
assert valid_card('5457 6238 1251 4311') is False
assert valid_card('3333 3333 3333 3331') is True
assert valid_card('6666 6666 6666 6664') is True
assert valid_card('5457 6238 0254 4311') is False
assert valid_card('0000 0000 0000 0000') is True
assert valid_card('5457 1111 9323 4311') is False
assert valid_card('5457 6238 9823 4311') is True
assert valid_card('1145 6238 9323 4311') is False
assert valid_card('8888 8888 8888 8888') is True
assert valid_card('0025 2521 9323 4311') is False
assert valid_card('5457 6238 9323 4311') is False
assert valid_card('1111 1111 1111 1117') is True
assert valid_card('1234 5678 9012 3452') is True
assert valid_card('5458 4444 9323 4311') is False
assert valid_card('5457 6238 3333 4311') is False
assert valid_card('0123 4567 8901 2345') is False
assert valid_card('5555 5555 5555 5557') is True
