from collections import Counter
from itertools import chain


def id_best_users(*args):
    best_users = set.intersection(*(set(a) for a in args))
    cnt = Counter(chain(*args))
    users = {}
    for k, v in cnt.iteritems():
        if k in best_users:
            users.setdefault(v, []).append(k)
    return [[k, sorted(v)] for k, v in sorted(users.iteritems(), reverse=True)]
