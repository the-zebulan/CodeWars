def sort_me(lst):
    lst.sort(key=lambda a: str(a)[-1])
    return lst
    # return sorted(key=lambda a: str(a)[-1])


assert sort_me(['acvd', 'bcc']) == ['bcc', 'acvd']
assert sort_me(['asdf', 14, '13', 'asdf']) == ['13', 14, 'asdf', 'asdf']
