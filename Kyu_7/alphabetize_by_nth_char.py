from operator import itemgetter


def sort_it(lst, n):
    return ', '.join(sorted(lst.split(', '), key=itemgetter(n - 1)))
