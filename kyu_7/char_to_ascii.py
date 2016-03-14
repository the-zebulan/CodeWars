def char_to_ascii(string):
    return {a: ord(a) for a in set(string) if a.isalpha()} or None
