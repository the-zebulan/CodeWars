def feuer_frei(concentration, barrels):
    fuel_hours = barrels * concentration
    if fuel_hours < 100:
        return '{} Stunden mehr Benzin ben\xf6tigt.'.format(100 - fuel_hours)
    elif fuel_hours == 100:
        return 'Perfekt!'
    return fuel_hours - 100
