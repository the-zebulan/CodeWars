def only_az(s):
    return ''.join(a for a in s if a.isalpha())


def autocomplete(s, lst):
    s = only_az(s)
    return [a for a in lst if only_az(a).lower().startswith(s)][:5]
