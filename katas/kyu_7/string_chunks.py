def string_chunk(strng, n=0):
    try:
        return [strng[a:a + n] for a in xrange(0, len(strng), n)]
    except (TypeError, ValueError):
        return []
