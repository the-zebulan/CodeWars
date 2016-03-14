def from_seconds(seconds):
    h, seconds = divmod(seconds, 3600)
    m, seconds = divmod(seconds, 60)
    return '|'.join('{:0>2.0f}'.format(a) for a in (h, m, seconds))


def to_seconds(h, m, s):
    return h * 3600 + m * 60 + s


def stat(string):
    if not string:
        return ''
    times = []
    total_sum = total_racers = 0
    for b in string.split(', '):
        seconds = to_seconds(*(int(c) for c in b.split('|')))
        total_racers += 1
        total_sum += seconds
        times.append(seconds)

    times.sort()
    maximum = times[-1]
    minimum = times[0]
    q, r = divmod(total_racers, 2)
    return 'Range: {} Average: {} Median: {}'.format(
        from_seconds(maximum - minimum),
        from_seconds(int(total_sum / float(total_racers))),
        from_seconds(sum(times[q - 1:q + 1]) / 2 if not r else times[q])
    )
