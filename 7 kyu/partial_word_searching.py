def word_search(query, seq):
    query = query.lower()
    return filter(lambda a: query in a.lower(), seq) or ['None']

assert word_search("ab", ["za", "ab", "abc", "zab", "zbc"]) == \
    ["ab", "abc", "zab"]
assert word_search("aB", ["za", "ab", "abc", "zab", "zbc"]) == \
    ["ab", "abc", "zab"]
assert word_search("XX", ["za", "ab", "abc", "zab", "zbc"]) == ['None']
