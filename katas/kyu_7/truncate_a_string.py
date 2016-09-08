def truncate_string(s, max_len):
    if len(s) <= max_len:
        return s
    return '{}...'.format(s[:max_len - (3 if max_len > 3 else 0)])
