def weather_info(temp):
    celsius = (temp - 32) * (5 / 9.0)
    if celsius > 0:
        return '{} is above freezing temperature'.format(celsius)
    return '{} is freezing temperature'.format(celsius)

assert weather_info(50) == '10.0 is above freezing temperature'
assert weather_info(23) == '-5.0 is freezing temperature'
