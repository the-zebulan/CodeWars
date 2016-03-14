from re import compile, match, IGNORECASE
from time import strftime, strptime

REGEX_12 = compile(r'[0-1]*\d:[0-5]\d(am|pm)', IGNORECASE)
REGEX_24 = compile(r'[0-2]\d:[0-5]\d$')


def convert_time(output_format, input_time):
    if output_format not in ('12', '24'):
        return False
    elif match(REGEX_12, input_time):
        if output_format == '24':
            return strftime('%H:%M', strptime(input_time, '%I:%M%p'))
        return input_time
    elif match(REGEX_24, input_time):
        if output_format == '12':
            return strftime('%I:%M%p', strptime(input_time, '%H:%M'))
        return input_time
    return False
