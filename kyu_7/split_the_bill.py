def split_the_bill(x):
    people = total = 0
    for k, v in x.iteritems():
        people += 1
        total += v
    average = total / float(people)
    return {k: round(v - average, 2) for k, v in x.iteritems()}
