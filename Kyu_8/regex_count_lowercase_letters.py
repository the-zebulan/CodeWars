def lowercase_count(strng):
    return sum(a.islower() for a in strng)


assert lowercase_count("abc") == 3
assert lowercase_count("abcABC123") == 3
assert lowercase_count("abcABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~") == 3
assert lowercase_count("") == 0
assert lowercase_count("ABC123!@#$%^&*()_-+=}{[]|\':;?/>.<,~") == 0
assert lowercase_count("abcdefghijklmnopqrstuvwxyz") == 26
