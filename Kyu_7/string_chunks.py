def string_chunk(string, n=0):
    try:
        return [string[a:a + n] for a in xrange(0, len(string), n)]
    except (TypeError, ValueError):
        return []
