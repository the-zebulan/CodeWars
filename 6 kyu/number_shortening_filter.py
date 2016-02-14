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


filter1 = shorten_number(['', 'k', 'm'], 1000)
assert filter1('234324') == '234k'
assert filter1('98234324') == '98m'
assert filter1([1, 2, 3]) == '[1, 2, 3]'
filter2 = shorten_number(['B', 'KB', 'MB', 'GB'], 1024)
assert filter2('32') == '32B'
assert filter2('2100') == '2KB'
assert filter2('pippi') == 'pippi'
