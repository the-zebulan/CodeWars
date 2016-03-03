def make_sentences(parts):
    return '{}.'.format(
        ''.join(' ' + a if a.isalnum() else a for a in parts).strip(' .'))


assert make_sentences(['hello', 'world']) == 'hello world.'
assert make_sentences(
    ['Quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']) \
    == 'Quick brown fox jumped over the lazy dog.'
assert make_sentences(['hello', ',', 'my', 'dear']) == 'hello, my dear.'
assert make_sentences(['one', ',', 'two', ',', 'three']) == 'one, two, three.'
assert make_sentences(
    ['One', ',', 'two', 'two', ',', 'three', 'three', 'three', ',', '4', '4',
     '4', '4']) == 'One, two two, three three three, 4 4 4 4.'
assert make_sentences(['hello', 'world', '.']) == 'hello world.'
assert make_sentences(['Bye', '.']) == 'Bye.'
assert make_sentences(['hello', 'world', '.', '.', '.']) == 'hello world.'
assert make_sentences(
    ['The', 'Earth', 'rotates', 'around', 'The', 'Sun', 'in', '365', 'days',
     ',', 'I', 'know', 'that', '.', '.', '.', '.', '.', '.', '.', '.', '.',
     '.', '.', '.']) \
    == 'The Earth rotates around The Sun in 365 days, I know that.'
