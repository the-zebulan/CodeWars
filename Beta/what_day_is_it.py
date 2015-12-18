from datetime import datetime

WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday')


def day(date):
    return WEEKDAYS[datetime.strptime(date, '%Y%m%d').weekday()]


assert day("20151208") == "Tuesday"
assert day("20140728") == "Monday"
assert day("20160229") == "Monday"
assert day("20160301") == "Tuesday"
assert day("19000228") == "Wednesday"
assert day("19000301") == "Thursday"
