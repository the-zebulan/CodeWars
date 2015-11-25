def guess_my_number(guess, number='123-451-2345'):
    return ''.join(a if a in guess + '-' else '#' for a in number)


assert guess_my_number('0') == '###-###-####'
assert guess_my_number('01') == '1##-##1-####'
assert guess_my_number('012') == '12#-##1-2###'
assert guess_my_number('0123') == '123-##1-23##'
assert guess_my_number('01234') == '123-4#1-234#'
assert guess_my_number('012345') == '123-451-2345'
