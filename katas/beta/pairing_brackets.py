def bracket_pairs(strng):
    matching_indexes = {}
    open_indexes = []
    for i, a in enumerate(strng):
        if a == '(':
            open_indexes.append(i)
        elif a == ')':
            try:
                matching_indexes[open_indexes.pop()] = i
            except IndexError:
                return False
    return matching_indexes if not open_indexes else False
