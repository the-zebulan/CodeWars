from re import compile, match, I

regex = compile(r'((Jo\w+).* (Jo\w+$|\w+Jo))|((Gio\w+).* (Gio\w+$|\w+Gio))', I)
# 'regex' should equal REGEX
# PEP8 - Constants are written in UPPERCASE with underscores separating words


def is_jojo(name):
    return bool(match(regex, name))


print is_jojo("Jonathan Joestar") is True
print is_jojo("Dio Brando") is False
