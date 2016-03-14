from datetime import datetime

OUTPUT = '{} has {} days'.format


def year_days(year):
    if not year:
        return OUTPUT(year, 366)
    y = abs(year)
    return OUTPUT(year, (datetime(y + 1, 1, 1) -
                         datetime(y, 1, 1)).days)
