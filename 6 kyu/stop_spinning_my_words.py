def spin_words(sentence):
    return ' '.join(a if len(a) < 5 else a[::-1] for a in sentence.split())

assert spin_words('Welcome') == 'emocleW'
assert spin_words('Hey fellow warriors') == 'Hey wollef sroirraw'
assert spin_words('This is a test') == 'This is a test'
assert spin_words('This is another test') == 'This is rehtona test'
