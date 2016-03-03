from datetime import datetime

WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday')


def day(date):
    return WEEKDAYS[datetime.strptime(date, '%Y%m%d').weekday()]
