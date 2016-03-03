def make_readable(seconds):
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)


assert make_readable(0) == '00:00:00'
assert make_readable(5) == '00:00:05'
assert make_readable(60) == '00:01:00'
assert make_readable(86399) == '23:59:59'
assert make_readable(359999) == '99:59:59'
