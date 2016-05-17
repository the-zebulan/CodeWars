def lose_weight(gender, weight, duration):
    if gender not in 'MF':
        return 'Invalid gender'
    elif duration <= 0:
        return 'Invalid duration'
    elif weight <= 0:
        return 'Invalid weight'
    return round(weight * ((0.988, 0.985)[gender == 'M'] ** duration), 1)
