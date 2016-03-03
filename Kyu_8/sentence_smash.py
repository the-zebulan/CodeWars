# def smash(words):
#     return ' '.join(words)

# smash = lambda words: ' '.join(words)

smash = ' '.join

assert smash(['hello']) == 'hello'
assert smash(['hello', 'world']) == 'hello world'
