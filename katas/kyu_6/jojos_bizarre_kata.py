from re import compile, match, I

regex = compile(r'((Jo\w+).* (Jo\w+$|\w+Jo))|((Gio\w+).* (Gio\w+$|\w+Gio))', I)


def is_jojo(name):
    return bool(match(regex, name))
