from re import compile, match

REGEX = compile(r'^(?P<h>\d{2}):(?P<m>[0-5]\d):(?P<s>[0-5]\d)$')


def to_seconds(time):
    m = match(REGEX, time)
    if m and time[slice(*m.span())] == time:
        hms = m.groupdict()
        return int(hms['h']) * 3600 + int(hms['m']) * 60 + int(hms['s'])


assert to_seconds("00:00:00") == 0
assert to_seconds("01:02:03") == 3723
assert to_seconds("01:02:60") is None
assert to_seconds("01:60:03") is None
assert to_seconds("99:59:59") == 359999
assert to_seconds("0:00:00") is None
assert to_seconds("00:0:00") is None
assert to_seconds("00:00:0") is None
assert to_seconds("00:00:00\n") is None
assert to_seconds("\n00:00:00") is None
