from datetime import date


def days_until_christmas(day):
    christmas = date(day.year, 12, 25)
    if day > christmas:
        christmas = date(day.year + 1, 12, 25)
    return (christmas - day).days
