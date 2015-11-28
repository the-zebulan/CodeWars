def make_string(s):
    return ''.join(a[0] for a in s.split())


assert make_string("sees eyes xray yoat") == "sexy"
assert make_string("brown eyes are nice") == "bean"
assert make_string("cars are very nice") == "cavn"
assert make_string("kaks de gan has a big head") == "kdghabh"
