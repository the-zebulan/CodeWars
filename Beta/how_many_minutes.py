from datetime import datetime


def date_to_mins(date):
    try:
        day = datetime.strptime(date, '%m/%d/%Y')
    except ValueError:
        return -1
    return (day - datetime(day.year, 1, 1)).total_seconds() / 60 + 1440


assert date_to_mins('02/10/2016') == 59040
assert date_to_mins('02/29/2016') == 86400
# I think this third test case is wrong in the kata, issue raised on CodeWars
print date_to_mins('04/21/2016')  # == 159840  # <-- should be 161280?
assert date_to_mins('05/31/2016') == 218880
