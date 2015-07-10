def lovefunc(flower, flower2):
    return (flower + flower2) % 2 != 0

assert lovefunc(1, 4) is True
assert lovefunc(2, 2) is False
assert lovefunc(0, 1) is True
assert lovefunc(0, 0) is False
