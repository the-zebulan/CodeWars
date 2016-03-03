def string_chunk(string, n=0):
    try:
        return [string[a:a + n] for a in xrange(0, len(string), n)]
    except (TypeError, ValueError):
        return []

assert string_chunk('codewars', 2) == ['co', 'de', 'wa', 'rs']
assert string_chunk('thiskataeasy', 4) == ['this', 'kata', 'easy']
assert string_chunk('hello world', 3) == ['hel', 'lo ', 'wor', 'ld']
assert string_chunk('everlong', 100) == ['everlong']
