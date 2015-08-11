def filter_numbers(string):
    return ''.join(a for a in string if not a.isdigit())

assert filter_numbers("test123"), 'test'
assert filter_numbers("a1b2c3"), 'abc'
assert filter_numbers("aa1bb2cc3dd"), 'aabbccdd'
