def sort_list(sort_by, lst):
    return sorted(lst, key=lambda a: a[sort_by], reverse=True)
