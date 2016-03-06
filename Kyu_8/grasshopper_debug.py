def weather_info(temp):
    celsius = (temp - 32) * (5 / 9.0)
    if celsius > 0:
        return '{} is above freezing temperature'.format(celsius)
    return '{} is freezing temperature'.format(celsius)
