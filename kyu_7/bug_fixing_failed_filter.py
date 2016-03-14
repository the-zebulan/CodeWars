def filter_numbers(string):
    return ''.join(a for a in string if not a.isdigit())
