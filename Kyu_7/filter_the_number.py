def filter_string(string):
    return int(''.join(a for a in string if a.isdigit()))

assert filter_string("123") == 123
assert filter_string("a1b2c3") == 123
assert filter_string("aa1bb2cc3dd") == 123
assert filter_string("aa 112 3dd") == 1123
assert filter_string("11bb2c23c3") == 112233
