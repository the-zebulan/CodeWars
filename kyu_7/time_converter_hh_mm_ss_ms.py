from datetime import datetime


def convert(time):
    return '{:02}:{:02}:{:02},{:03}'.format(
        time.hour, time.minute, time.second, time.microsecond / 1000)
