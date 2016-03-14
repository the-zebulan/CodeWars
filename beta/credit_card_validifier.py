# from re import compile, match
#
# REGEXES = {compile('6011\d{12}'): 'Discover',
#            compile('3[47]\d{13}'): 'AMEX',
#            compile('5[1-5]\d{14}'): 'Master',
#            compile('4\d{12}'): 'VISA', compile('4\d{15}'): 'VISA'}
#
#
# def credit(num):
#     num = str(num)
#     for regex, card_type in REGEXES.iteritems():
#         if match(regex, num):
#             return card_type
#     return 'Invalid'


def credit(num):
    num = str(num)
    length = len(num)
    if num.startswith('6011') and length == 16:
        return 'Discover'
    elif num.startswith(('34', '37')) and length == 15:
        return 'AMEX'
    elif 51 <= int(num[:2]) <= 55 and length == 16:
        return 'Master'
    elif num.startswith('4') and length in (13, 16):
        return 'VISA'
    return 'Invalid'
