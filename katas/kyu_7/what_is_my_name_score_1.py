# for testing only, 'alpha' is included in the preloaded section on Codewars
alpha = {'ABCDE': 1, 'FGHIJ': 2, 'KLMNO': 3, 'PQRST': 4, 'UVWXY': 5}


def name_score(name):
    scores = {k: v for keys, v in alpha.iteritems() for k in keys}
    return {name: sum(scores.get(a, 0) for a in name.upper())}
