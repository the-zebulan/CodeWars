def cypher(text):
    d = dict(zip('IREASGTBOlzeasbtgo', '123456780123456790'))
    return ''.join(d.get(a, a) for a in text)
