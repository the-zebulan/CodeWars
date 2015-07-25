HUMAN = {1: 'second', 60: 'minute', 3600: 'hour',
         86400: 'day', 604800: 'week'}
KEYS = sorted(HUMAN.keys(), reverse=True)
OUTPUT = '{} {}{} ago'.format


def to_pretty(seconds):
    if seconds == 0:
        return 'just now'
    for key in KEYS:
        quo, rem = divmod(seconds, key)
        if quo:
            if quo == 1:  # singular
                a = 'an' if key == 3600 else 'a'
                b = ''
            elif quo > 1:
                a = quo
                b = 's'
            return OUTPUT(a, HUMAN[key], b)

assert to_pretty(300) == '5 minutes ago'
assert to_pretty(60) == 'a minute ago'
assert to_pretty(3600) == 'an hour ago'
