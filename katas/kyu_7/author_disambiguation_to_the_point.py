def could_be(original, another):
    if not original.strip() or not another.strip():
        return False
    return set(another.split()).issubset(original.split())
