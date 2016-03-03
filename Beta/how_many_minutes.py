from datetime import datetime


def date_to_mins(date):
    try:
        day = datetime.strptime(date, '%m/%d/%Y')
    except ValueError:
        return -1
    return (day - datetime(day.year, 1, 1)).total_seconds() / 60 + 1440
