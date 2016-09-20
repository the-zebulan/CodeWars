def replace_all(obj, old, new):
    if isinstance(obj, str):
        return obj.replace(old, new)
    return [new if a == old else a for a in obj]
