from re import compile, match

REGEX = compile(r'^(?P<h>\d{2}):(?P<m>[0-5]\d):(?P<s>[0-5]\d)$')


def to_seconds(time):
    m = match(REGEX, time)
    if m and time[slice(*m.span())] == time:
        hms = m.groupdict()
        return int(hms['h']) * 3600 + int(hms['m']) * 60 + int(hms['s'])
