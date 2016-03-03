def data_reverse(data):
    return [b for a in xrange(len(data) - 8, -1, -8) for b in data[a:a + 8]]
