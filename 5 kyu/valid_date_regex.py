from re import compile, X

valid_date = compile(r'''\[(
    # 31 days - January, March, May, July, August, October, December
    (0[13578]|1[02])-(0[1-9]|[1-2]\d|3[0-1])|

    # 30 days - April, June, September, November
    (0[469]|11)-(0[1-9]|[1-2]\d|30)|

    # 28 days - February
    02-(0[1-9]|1\d|2[0-8])
)\]''', X)


assert valid_date.search("[01-23]") is not None
assert valid_date.search("[02-31]") is None
assert valid_date.search("[02-16]") is not None
assert valid_date.search("[ 6-03]") is None
assert valid_date.search("ignored [08-11] ignored") is not None
assert valid_date.search("[3] [12-04] [09-tenth]") is not None
assert valid_date.search("[02-00]") is None
assert valid_date.search("[[[08-29]]]") is not None
assert valid_date.search("[13-02]") is None
assert valid_date.search("[02-[08-11]04]") is not None
