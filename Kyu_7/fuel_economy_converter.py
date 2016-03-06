LITRES_PER_GALLON = 3.785411784
KMS_PER_MILE = 1.609344


def mpg2lp100km(mpg):
    """ mpg_to_litres_per_100km == PEP8 """
    return round(LITRES_PER_GALLON / ((mpg * KMS_PER_MILE) / 100), 2)


def lp100km2mpg(lp100km):
    """ litres_per_100_km_to_mpg == PEP8 """
    return round((100 / KMS_PER_MILE) / (lp100km / LITRES_PER_GALLON), 2)
