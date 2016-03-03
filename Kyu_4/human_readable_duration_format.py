IN_SECONDS = (('year', 31536000), ('day', 86400), ('hour', 3600),
              ('minute', 60), ('second', 1))


def format_duration(seconds):
    if not seconds:
        return 'now'
    times = []
    words = 0
    for name, num in IN_SECONDS:
        q, seconds = divmod(seconds, num)
        if q:
            times.append('{} {}{}'.format(q, name, 's' if q > 1 else ''))
            words += 1
    return times[0] if words == 1 else \
        '{} and {}'.format(', '.join(times[:-1]), times[-1])


assert format_duration(1) == "1 second"
assert format_duration(62) == "1 minute and 2 seconds"
assert format_duration(120) == "2 minutes"
assert format_duration(3600) == "1 hour"
assert format_duration(3662) == "1 hour, 1 minute and 2 seconds"
