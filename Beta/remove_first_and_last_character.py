def remove_char(s):
    return s[1:-1]


assert remove_char('eloquent') == 'loquen'
assert remove_char('country') == 'ountr'
assert remove_char('person') == 'erso'
assert remove_char('place') == 'lac'
assert remove_char('ok') == ''
