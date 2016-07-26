def ReOrdering(name):
    """ re_ordering or reordering == PEP8 (forced PascalCase by Codewars) """
    return ' '.join(sorted(name.split(), key=lambda a: a[0].islower()))
