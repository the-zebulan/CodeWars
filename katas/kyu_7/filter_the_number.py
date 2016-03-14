def filter_string(string):
    return int(''.join(a for a in string if a.isdigit()))
