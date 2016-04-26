import re

IS_VALID = re.compile(r'\d{4} \d{4}\Z')
HAS_VALID = re.compile(r'\d{4} \d{4}')


def is_valid_HK_phone_number(number):
    return bool(IS_VALID.match(number))


def has_valid_HK_phone_number(number):
    return bool(HAS_VALID.search(number))
