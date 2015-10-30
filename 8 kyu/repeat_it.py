def repeat_it(string, n):
    return string * n if isinstance(string, str) else 'Not a string'


assert repeat_it('*', 3) == '***'
assert repeat_it('Hello', 11) \
    == 'HelloHelloHelloHelloHelloHelloHelloHelloHelloHelloHello'
