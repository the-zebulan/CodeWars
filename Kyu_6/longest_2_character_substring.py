def substring(string):
    if not string:
        return ''
    length = len(string)
    longest_sub = 0
    sub_strings = []
    for a in xrange(length):
        unique = set()
        for b in xrange(a, length):
            unique.add(string[b])
            if len(unique) > 2:
                break
            if b + 1 - a == longest_sub:
                sub_strings.append(string[a:b + 1])
            if b + 1 - a > longest_sub:
                longest_sub = b + 1 - a
                sub_strings = [string[a:b + 1]]
    return sub_strings[0]


assert substring("") == ""
assert substring("a") == "a"
assert substring("aa") == "aa"
assert substring("aaa") == "aaa"
assert substring("ab") == "ab"
assert substring("aba") == "aba"
assert substring("abc") == "ab"
assert substring("abacd") == "aba"
assert substring("abcba") == "bcb"
assert substring("bbacc") == "bba"
assert substring("ccddeeff") == "ccdd"
assert substring("abacddcd") == "cddcd"
assert substring("cefageaacceaccacca") == "accacca"
