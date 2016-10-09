def cat_mouse(s, j):
    indexes = {a: i for i, a in enumerate(s)}
    cat = indexes.get('C')
    dog = indexes.get('D')
    mouse = indexes.get('m')
    if cat is None or dog is None or mouse is None:
        return 'boring without all three'
    elif abs(cat - mouse) <= j + 1:
        if cat < dog < mouse or mouse < dog < cat:
            return 'Protected!'
        return 'Caught!'
    return 'Escaped!'
