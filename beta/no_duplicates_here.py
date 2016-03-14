def list_de_dup(lst):
    return sorted(set(a for a in lst if a is not None)) \
        if isinstance(lst, list) else 'Not an array'
