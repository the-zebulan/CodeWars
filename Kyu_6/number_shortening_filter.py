def shorten_number(suffixes, base):
    def inner(num):
        try:
            num = int(num)
        except (TypeError, ValueError):
            return str(num)

        for a in xrange(len(suffixes) - 1, -1, -1):
            b = num / base ** a
            if b:
                return '{}{}'.format(b, suffixes[a])

    return inner
