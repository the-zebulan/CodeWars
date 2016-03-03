from re import compile, finditer, I

REGEX = compile(r'(?P<water>(water|wet|wash)[a-zA-Z]*)|'
                r'(?P<slime>(I don\'t know|slime))', I)


def bucket_of(said):
    has_slime = has_water = False
    for m in finditer(REGEX, said):
        d = m.groupdict()
        if d['slime'] is not None:
            has_slime = True
        if d['water'] is not None:
            has_water = True
    if has_slime and has_water:
        return 'sludge'
    elif has_slime:
        return 'slime'
    elif has_water:
        return 'water'
    return 'air'


assert bucket_of('wet water') == 'water'
assert bucket_of('slime water') == 'sludge'
assert bucket_of('I don\'t know if this will work') == 'slime'
assert bucket_of(
    'I don\'t know if this will work without watering it first.') == 'sludge'
assert bucket_of('') == 'air'
assert bucket_of('slimeslimeslimeslimewater') == 'sludge'
