from re import compile, match

REGEX = compile(r'((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){4}$')


def ipv4_address(address):
    # refactored thanks to @leonoverweel on CodeWars
    return bool(match(REGEX, address + '.'))


assert ipv4_address('') is False
assert ipv4_address('127.0.0.1') is True
assert ipv4_address('0.0.0.0') is True
assert ipv4_address('255.255.255.255') is True
assert ipv4_address('10.20.30.40') is True
assert ipv4_address('10.256.30.40') is False
assert ipv4_address('10.20.030.40') is False
assert ipv4_address('127.0.1') is False
assert ipv4_address('127.0.0.0.1') is False
assert ipv4_address('..255.255') is False
assert ipv4_address('127.0.0.1\n') is False
assert ipv4_address('\n127.0.0.1') is False
assert ipv4_address(' 127.0.0.1') is False
assert ipv4_address('127.0.0.1 ') is False
assert ipv4_address(' 127.0.0.1 ') is False
