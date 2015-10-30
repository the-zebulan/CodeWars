def toJadenCase(string):
    """ to_jaden_case == PEP8 (forced mixedCase by CodeWars) """
    return ' '.join(a.capitalize() for a in string.split())


assert toJadenCase('How can mirrors be real if our eyes aren\'t real') == \
       'How Can Mirrors Be Real If Our Eyes Aren\'t Real'
