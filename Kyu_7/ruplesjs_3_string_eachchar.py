def each_char(s, arg):
    if isinstance(arg, str):
        return ''.join('{}{}'.format(a, arg) for a in s)
    return ''.join(arg(b) for b in s)


assert each_char('hello', ' ') == 'h e l l o '
assert each_char('hello', '123') == 'h123e123l123l123o123'
assert each_char('', '123') == ''
assert each_char('hello', lambda c: c.upper()) == 'HELLO'
assert each_char('H e l l o ', lambda c: '1' if c == ' ' else c) == \
    'H1e1l1l1o1'
assert each_char('I12 0ca431n35no55t 77re3321231ad 4t4h7771i888973s.',
                 lambda c: '' if c in '0123456789' else c) == \
    'I cannot read this.'
