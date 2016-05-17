def lose_weight(gender, weight, duration):
    if gender not in 'MF':
        return 'Invalid gender'
    elif duration <= 0:
        return 'Invalid duration'
    elif weight <= 0:
        return 'Invalid weight'
    percent = 0.015 if gender == 'M' else 0.012
    for _ in xrange(duration):
        weight -= weight * percent
    return round(weight, 1)
