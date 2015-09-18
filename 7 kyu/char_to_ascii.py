def char_to_ascii(string):
    return {a: ord(a) for a in set(string) if a.isalpha()} or None

assert char_to_ascii("") is None
assert char_to_ascii("a") == {"a": 97}
assert char_to_ascii("aaa") == {"a": 97}
