def to_weird_case(string):
    return ' '.join(''.join(a.upper() if i % 2 == 0 else a.lower() for i, a in
                            enumerate(word)) for word in string.split())
