def ranks(array):
    ranking = {}
    for i, a in enumerate(sorted(array, reverse=True), start=1):
        if a not in ranking:
            ranking[a] = i
    return [ranking[b] for b in array]
