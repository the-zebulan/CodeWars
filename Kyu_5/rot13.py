# from string import ascii_uppercase as up, ascii_lowercase as low, \
#     ascii_letters as az, maketrans
#
# ROT13 = maketrans(low[13:] + low[:13] + up[13:] + up[:13], az)
#
#
# def rot13(message):
#     return message.translate(ROT13)


def rot13(message):
    return message.encode('rot13')


assert rot13("EBG13 rknzcyr.") == "ROT13 example."
assert rot13("This is my first ROT13 excercise!") \
       == "Guvf vf zl svefg EBG13 rkprepvfr!"
assert rot13(
    'Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl\'f fubrf.') \
       == 'In the elevators, the extrovert looks at the OTHER guy\'s shoes.'
