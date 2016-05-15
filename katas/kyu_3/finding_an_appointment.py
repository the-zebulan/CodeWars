from itertools import groupby


def from_seconds(seconds):
    return '{:02}:{:02}'.format(*divmod(seconds, 60))


def to_seconds(hh_mm):
    h, m = (int(a) for a in hh_mm.split(':'))
    return h * 60 + m


def set_range(start_time, stop_time):
    return set(xrange(to_seconds(start_time), to_seconds(stop_time)))


def get_start_time(schedules, duration):
    free_time = set_range('09:00', '19:00')
    for person in schedules:
        for meeting in person:
            free_time.difference_update(set_range(*meeting))

    for k, g in groupby(enumerate(sorted(free_time)), lambda (i, x): i - x):
        _, first = last = next(g)
        for _, last in g:
            pass
        if last - first + 1 >= duration:
            return from_seconds(first)
