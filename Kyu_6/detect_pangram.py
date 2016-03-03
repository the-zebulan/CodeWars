from string import ascii_lowercase

AZ = set(ascii_lowercase)


def is_pangram(string):
    """ Thanks to 'hiasen' on CodeWars for the idea of using subset """
    return AZ.issubset(set(string.lower()))
    # return set(a for a in string.lower() if a.isalpha()) == AZ

assert is_pangram("The quick, brown fox jumps over the lazy dog!") is True
assert is_pangram('Cwm fjord bank glyphs vext quiz') is True
assert is_pangram('Pack my box with five dozen liquor jugs.') is True
assert is_pangram('How quickly daft jumping zebras vex.') is True
assert is_pangram('ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ') is True
assert is_pangram('This isn\'t a pangram!') is False
assert is_pangram('abcdefghijklmopqrstuvwxyz') is False
