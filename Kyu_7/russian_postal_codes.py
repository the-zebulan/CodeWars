# INVALID = {'0', '5', '7', '8', '9'}
#
#
# def zip_validate(postal_code):
#     length = 0
#     for i, a in enumerate(postal_code):
#         if i == 0 and a in INVALID or not a.isdigit():
#             return False
#         length += 1
#     return length == 6

from re import match


def zip_validate(postcode):
    return bool(match("^[12346][0-9]{5}$", postcode))
