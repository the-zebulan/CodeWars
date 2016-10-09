def paul(arr):
    scores = {'kata': 5, 'Petes kata': 10, 'eating': 1}
    result = sum(scores.get(a, 0) for a in arr)
    if result < 40:
        return 'Super happy!'
    elif result < 70:
        return 'Happy!'
    elif result < 100:
        return 'Sad!'
    return 'Miserable!'
