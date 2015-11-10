from re import compile, match, IGNORECASE
from time import strftime, strptime

REGEX_12 = compile(r'[0-1]*\d:[0-5]\d(am|pm)', IGNORECASE)
REGEX_24 = compile(r'[0-2]\d:[0-5]\d$')


def convert_time(output_format, time):
    if output_format not in ('12', '24'):
        return False
    elif match(REGEX_12, time):
        if output_format == '24':
            return strftime('%H:%M', strptime(time, '%I:%M%p'))
        return time
    elif match(REGEX_24, time):
        if output_format == '12':
            return strftime('%I:%M%p', strptime(time, '%H:%M'))
        return time
    return False


assert convert_time("24", "09:00AM") == "09:00"
assert convert_time("24", "09:00PM") == "21:00"
assert convert_time("12", "08:13AM") == "08:13AM"
assert convert_time("12", "05:19PM") == "05:19PM"
assert convert_time("12", "21:13") == "09:13PM"
