SCORE = {'O': '0', 'o': '0', 'k': '1'}


def okkOokOo(s):
    """ okkookoo == PEP8, forced mixedCase by CodeWars """
    return ''.join(chr(int(''.join(SCORE.get(a, '') for a in word), 2))
                   for word in s.split('?'))


assert okkOokOo('Ok, Ook, Ooo!') == 'H'
assert okkOokOo('Ok, Ook, Ooo?  Okk, Ook, Ok?  Okk, Okk, Oo?  Okk, Okk, Oo?'
                '  Okk, Okkkk!') == 'Hello'
assert okkOokOo('Ok, Ok, Okkk?  Okk, Okkkk?  Okkk, Ook, O?  Okk, Okk, Oo?'
                '  Okk, Ook, Oo?  Ook, Ooook!') == 'World!'
