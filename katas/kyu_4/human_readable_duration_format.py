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
