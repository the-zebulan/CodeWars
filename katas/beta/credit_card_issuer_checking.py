import re

REGEX = re.compile(r'''
(?P<AMEX>3[47]\d{13}$) |
(?P<Discover>6011\d{12}$) |
(?P<Mastercard>5[1-5]\d{14}$) |
(?P<VISA>(?:4\d{15}|4\d{12})$)''', re.VERBOSE)


def get_issuer(card_num):
    try:
        return next(
            k for k, v in REGEX.match(str(card_num)).groupdict().iteritems()
            if v is not None
        )
    except AttributeError:
        return 'Unknown'
