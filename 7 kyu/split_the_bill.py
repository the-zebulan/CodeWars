def split_the_bill(x):
    people = total = 0
    for k, v in x.iteritems():
        people += 1
        total += v
    average = total / float(people)
    return {k: round(v - average, 2) for k, v in x.iteritems()}


assert split_the_bill({'A': 20, 'B': 15, 'C': 10}) \
    == {'A': 5, 'B': 0, 'C': -5}
assert split_the_bill({'A': 40, 'B': 25, 'X': 10}) \
    == {'A': 15, 'B': 0, 'X': -15}
