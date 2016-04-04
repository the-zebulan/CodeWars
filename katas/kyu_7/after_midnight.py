WEEKDAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday')


def day_and_time(minutes):
    days, minutes = divmod(minutes, 1440)
    hours, minutes = divmod(minutes, 60)
    return '{} {:02}:{:02}'.format(WEEKDAYS[days % 7], hours, minutes)
