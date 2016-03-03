def longest(s1, s2):
    return ''.join(sorted(set(s1).union(s2)))


assert longest("aretheyhere", "yestheyarehere") == "aehrsty"
assert longest("loopingisfunbutdangerous", "lessdangerousthancoding") \
    == "abcdefghilnoprstu"
assert longest("inmanylanguages", "theresapairoffunctions") \
    == "acefghilmnoprstuy"
