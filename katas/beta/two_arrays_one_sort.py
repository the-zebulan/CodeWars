def linked_sort(a_to_sort, a_linked, key=None):
    d = dict(zip(a_linked, a_to_sort))
    a_to_sort.sort(key=key or str)
    a_linked.sort(key=lambda a: a_to_sort.index(d[a]))
    return a_to_sort
