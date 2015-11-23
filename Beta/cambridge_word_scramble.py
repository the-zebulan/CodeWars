from random import shuffle
from re import findall


def mix_words(s):
    result = []
    for word in findall(r"[\w']+|[ .,!?:;/-]", s):
        if len(word) > 3:
            orig = list(word[1:-1])
            mid = orig[:]
            while mid == orig:
                shuffle(mid)
            result.append('{}{}{}'.format(word[0], ''.join(mid), word[-1]))
        else:
            result.append(word)
    return ''.join(result)


result = mix_words('hello')
assert result != 'hello'
assert len(result) == 5
assert result[0] == 'h'
assert result[4] == 'o'
assert ''.join(sorted(result[1:4])) == 'ell'
result = mix_words('hello Pippi')
assert result != 'hello Pippi'
assert len(result) == 11
assert result[0] == 'h'
assert result[4] == 'o'
assert result[5] == ' '
assert result[6] == 'P'
assert result[10] == 'i'
assert ''.join(sorted(result[1:4])) == 'ell'
assert ''.join(sorted(result[7:10])) == 'ipp'
result = mix_words('hello, Pippi!')
assert result != 'hello, Pippi!'
assert len(result) == 13
assert result[0] == 'h'
assert result[4] == 'o'
assert result[5] == ','
assert result[6] == ' '
assert result[7] == 'P'
assert result[11] == 'i'
assert result[12] == '!'
assert ''.join(sorted(result[1:4])) == 'ell'
assert ''.join(sorted(result[8:11])) == 'ipp'
assert mix_words('Hi') == 'Hi'
assert mix_words('Hi!') == 'Hi!'
assert mix_words('Hey') == 'Hey'
assert mix_words('Hey?') == 'Hey?'
