DENSITY = {'H': 1.36, 'W': 1, 'A': 0.87, 'O': 0.8}


def separate_liquids(glass):
    if not glass:
        return []
    column = len(glass[0])
    liquids = sorted((b for a in glass for b in a), key=lambda c: DENSITY[c])
    return [liquids[d:d + column] for d in xrange(0, len(liquids), column)]
