def my_parse_int(string):
    try:
        return int(string)
    except ValueError:
        return 'NaN'


assert my_parse_int('1') == 1
assert my_parse_int('  1 ') == 1
assert my_parse_int('08') == 8
assert my_parse_int('5 friends') == 'NaN'
assert my_parse_int('16.5') == 'NaN'
