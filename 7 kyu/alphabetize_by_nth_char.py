from operator import itemgetter


def sort_it(lst, n):
    return ', '.join(sorted(lst.split(', '), key=itemgetter(n - 1)))

assert sort_it('bid, zag', 2) == 'zag, bid'
assert sort_it('bill, bell, ball, bull', 2) == 'ball, bell, bill, bull'
assert sort_it('cat, dog, eel, bee', 3) == 'bee, dog, eel, cat'
