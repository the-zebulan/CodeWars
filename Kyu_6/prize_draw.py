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
