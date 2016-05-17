def is_balanced(s, pairs):
    closing_chars = []
    pair_dict = dict(zip(pairs[::2], pairs[1::2]))
    keys = set(pair_dict.iterkeys())
    values = set(pair_dict.itervalues())
    for a in s:
        in_keys = a in keys
        in_values = a in values
        if in_keys and in_values:
            try:
                last = closing_chars[-1]
            except IndexError:
                last = None
            if last != a:
                closing_chars.append(pair_dict[a])
            elif a != closing_chars.pop():
                return False
        elif in_keys:
            closing_chars.append(pair_dict[a])
        elif in_values:
            try:
                if a == closing_chars.pop():
                    continue
            except IndexError:
                pass
            return False
    return not closing_chars
