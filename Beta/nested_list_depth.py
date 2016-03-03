def list_depth(lst):
    result = [list_depth(a) for a in lst if isinstance(a, list)]
    return 1 + max(result) if result else 1
