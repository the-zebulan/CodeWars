from re import compile, sub, DOTALL

REGEX = compile(r'/\*.*?\*/|//[^\n]+', DOTALL)


def strip_it(code):
    return sub(REGEX, '', code)


assert strip_it("var Foo = 1;// Foo declared") == "var Foo = 1;"
assert strip_it("1 + /* 2 */3") == "1 + 3"
assert strip_it('1 /* a */+/* b */ 1') == "1 + 1"
assert strip_it(" x = 10;// ten !") == " x = 10;"
