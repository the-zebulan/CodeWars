from re import sub


def seven_ate9(string):
    return sub('(?<=7)9+(?=7)', '', string)

assert seven_ate9('79797') == '777'
assert seven_ate9('12345') == '12345'
