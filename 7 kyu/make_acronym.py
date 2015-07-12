def make_acronym(phrase):
    if not isinstance(phrase, str):
        return 'Not a string'
    words = phrase.split()
    result = []
    for word in words:
        if not word.isalpha():
            return 'Not letters'
        result.append(word[0].upper())
    return ''.join(result)

assert make_acronym('Hello codewarrior') == 'HC'
assert make_acronym('a42') == 'Not letters'
assert make_acronym(42) == 'Not a string'
assert make_acronym([2, 12]) == 'Not a string'
assert make_acronym({'name': 'Abraham'}) == 'Not a string'
