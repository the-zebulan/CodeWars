from re import compile, X

valid_date = compile(r'''\[(
    # 31 days - January, March, May, July, August, October, December
    (0[13578]|1[02])-(0[1-9]|[1-2]\d|3[0-1])|

    # 30 days - April, June, September, November
    (0[469]|11)-(0[1-9]|[1-2]\d|30)|

    # 28 days - February
    02-(0[1-9]|1\d|2[0-8])
)\]''', X)
