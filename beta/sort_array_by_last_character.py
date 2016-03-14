def sort_me(lst):
    lst.sort(key=lambda a: str(a)[-1])
    return lst
    # return sorted(key=lambda a: str(a)[-1])
