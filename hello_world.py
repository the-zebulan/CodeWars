def greet():
    ascii = [104, 3, 7, 0, 3, 79, 87, 8, 3, 6, -8]
    current = 0
    phrase = ''
    for dex, a in enumerate(ascii):
        current = current + a if dex % 2 == 0 else current - a
        phrase += chr(current)
    return phrase

assert greet() == 'hello world'
