def alex_mistakes(katas, minutes):
    mistakes = 0
    pushup_mins = 5
    remaining_mins = minutes - (6 * katas)
    while remaining_mins >= pushup_mins:
        mistakes += 1
        remaining_mins -= pushup_mins
        pushup_mins *= 2
    return mistakes
