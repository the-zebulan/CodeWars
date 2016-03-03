def evaporator(content, evap_per_day, threshold):
    day = 0
    evap_per_day /= 100.0
    threshold = content * (threshold / 100.0)
    while content >= threshold:
        content -= content * evap_per_day
        day += 1
    return day

assert evaporator(10, 10, 10) == 22
