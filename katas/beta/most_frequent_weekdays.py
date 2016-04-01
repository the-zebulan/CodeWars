from calendar import weekday

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
        'Friday', 'Saturday', 'Sunday']


def most_frequent_days(year):
    beg = weekday(year, 1, 1)
    end = weekday(year, 12, 31)
    return DAYS[beg:end + 1] if beg <= end else DAYS[:end + 1] + DAYS[beg:]
