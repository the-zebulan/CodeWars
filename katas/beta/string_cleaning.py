def string_clean(s):
    return ''.join(a for a in s if not a.isdigit())
