def to_weird_case(string):
    return ' '.join(''.join(a.upper() if i % 2 == 0 else a.lower() for i, a in
                            enumerate(word)) for word in string.split())

assert to_weird_case('This') == 'ThIs'
assert to_weird_case('is') == 'Is'
assert to_weird_case('This is a test') == 'ThIs Is A TeSt'
