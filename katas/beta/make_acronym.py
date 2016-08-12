def to_acronym(input_str):
    return ''.join(a[0].upper() for a in input_str.split())
