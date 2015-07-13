INVALID = {'0', '5', '7', '8', '9'}


def zip_validate(postal_code):
    length = 0
    for i, a in enumerate(postal_code):
        if i == 0 and a in INVALID or not a.isdigit():
            return False
        length += 1
    return length == 6

assert zip_validate('198328')
assert zip_validate('310003')
assert zip_validate('424000')
assert not zip_validate('12A483')
assert not zip_validate('1@63')
assert not zip_validate('111')
assert not zip_validate('056879')
assert not zip_validate('1111111')
