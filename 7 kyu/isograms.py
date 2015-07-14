def is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))

assert is_isogram("Dermatoglyphics") is True
assert is_isogram("isogram") is True
assert is_isogram("aba") is False
assert is_isogram("moOse") is False
assert is_isogram("isIsogram") is False
assert is_isogram("") is True
