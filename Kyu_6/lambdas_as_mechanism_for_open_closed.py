spoken = lambda greeting: '{}.'.format(greeting.capitalize())
shouted = lambda greeting: '{}!'.format(greeting.upper())
whispered = lambda greeting: '{}.'.format(greeting.lower())

greet = lambda style, msg: style(msg)

assert greet(spoken, "Hello") == "Hello."
assert greet(shouted, "Hello") == "HELLO!"
assert greet(whispered, "Hello") == "hello."
