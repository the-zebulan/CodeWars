def naughty_or_nice(data):
    naughty = nice = 0
    for month in data.itervalues():
        for day in month.itervalues():
            if day == 'Naughty':
                naughty += 1
            else:
                nice += 1
    return ('Naughty!', 'Nice!')[nice >= naughty]
