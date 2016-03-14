from operator import itemgetter


def sort_dict(d):
    return sorted(d.items(), key=itemgetter(1), reverse=True)
