def rank(names, weights, n):
    if not names:
        return 'No participants'
    scores = []
    for i, (name, weight) in enumerate(zip(names.split(','), weights), 1):
        current_rank = sum(1 + ord(a) - 64 for a in name.upper()) * weight
        scores.append((current_rank, name))
    else:
        if n > i:
            return 'Not enough participants'
    return sorted(scores, key=lambda (score, name): (-score, name))[n - 1][1]


assert rank('Elijah,Chloe,Elizabeth,Matthew,Natalie,Jayden',
            [1, 3, 5, 5, 3, 6], 2) == 'Matthew'
assert rank('COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH',
            [1, 4, 4, 5, 2, 1], 4) == 'PauL'
assert rank('Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin',
            [4, 2, 1, 4, 3, 1, 2], 4) == 'Benjamin'
assert rank('Lagon,Lily', [1, 5], 2) == 'Lagon'
assert rank('Addison,Jayden,Sofia,Michael,Andrew,Lily,Benjamin',
            [4, 2, 1, 4, 3, 1, 2], 8) == 'Not enough participants'
assert rank('', [4, 2, 1, 4, 3, 1, 2], 6) == 'No participants'
