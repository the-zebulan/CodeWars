from re import split


def drop_cap(string):
    return ''.join(a.capitalize() if not a.isspace() and len(a) > 2 else a
                   for a in split(r'(\s+)', string))
