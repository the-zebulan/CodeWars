def find_secret_message(paragraph):
    unique = set()
    result = []
    for word in (a.strip('.,:!?').lower() for a in paragraph.split()):
        if word in unique and word not in result:
            result.append(word)
        unique.add(word)
    return ' '.join(result)

assert find_secret_message(
    'thing sleeps is in, HAVE, always? in thing out is: WANTS a! good T-Rex'
    ', is, never, sleeps good NEVER, chocolate? Think the in Is THING? thing:'
    ' Pippi? sleeps T-Rex') == 'in thing is sleeps good never t-rex'
assert find_secret_message('This is a test. this test is fun.') == \
    'this test is'
assert find_secret_message('asdf qwer zxcv. zxcv fdsa rewq. qazw asdf sxed. '
                           'qwer crfv.') == 'zxcv asdf qwer'
