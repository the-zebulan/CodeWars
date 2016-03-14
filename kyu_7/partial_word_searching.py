def word_search(query, seq):
    query = query.lower()
    return filter(lambda a: query in a.lower(), seq) or ['None']
