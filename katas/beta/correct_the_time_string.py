from re import match


def to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds


def from_seconds(seconds):
    _, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)


def time_correct(t):
    if not t:
        return t
    m = match('(\d{2}):(\d{2}):(\d{2})$', t)
    if m:
        return from_seconds(to_seconds(*(int(a) for a in m.groups())))
