OUTPUT = '{0}{0}'.format


def double_char(s):
    return ''.join(OUTPUT(a) for a in s)


assert double_char('String') == 'SSttrriinngg'
assert double_char('Hello World') == 'HHeelllloo  WWoorrlldd'
assert double_char('1234!_ ') == '11223344!!__  '
