from re import compile, match

REGEX = compile(r'[a-zA-Z]\w*@[\w-]+(\.\w+)+$')


def validate(email):
    return bool(match(REGEX, email))


assert validate('abc@example.com') is True
assert validate('_bc@example.com') is False
assert validate('sa5 2erd76n@c7ws07u.mobi') is False
assert validate('5@a74qljvkfj.it') is False
