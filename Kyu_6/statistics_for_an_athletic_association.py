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


assert stat("01|15|59, 1|47|16, 01|17|20, 1|32|34, 2|17|17") \
    == "Range: 01|01|18 Average: 01|38|05 Median: 01|32|34"
assert stat("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41")\
    == "Range: 00|31|17 Average: 02|26|18 Median: 02|22|00"
