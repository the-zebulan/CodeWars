from re import compile, match

REGEX = compile(r'((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}'
                r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)$')


def is_valid_IP(strng):
    """ is_valid_ip == PEP8 (forced mixedCase by CodeWars) """
    return bool(match(REGEX, strng))

assert is_valid_IP('12.255.56.1') is True
assert is_valid_IP('') is False
assert is_valid_IP('abc.def.ghi.jkl') is False
assert is_valid_IP('123.456.789.0') is False
assert is_valid_IP('12.34.56') is False
assert is_valid_IP('12.34.56 .1') is False
assert is_valid_IP('12.34.56.-1') is False
assert is_valid_IP('123.045.067.089') is False
