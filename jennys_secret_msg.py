def greet(name):
    return "Hello, {}!".format('my love' if name == 'Johnny' else name)

assert greet('James') == 'Hello, James!'
assert greet('Johnny') == 'Hello, my love!'
