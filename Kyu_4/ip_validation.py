from re import compile, match

REGEX = compile(r'((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}'
                r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)$')


def is_valid_IP(strng):
    """ is_valid_ip == PEP8 (forced mixedCase by CodeWars) """
    return bool(match(REGEX, strng))
