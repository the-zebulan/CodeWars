GREET = 'Hello, {}!'.format


def greeting_for_all_friends(friends):
    return [GREET(a) for a in friends] if friends else None

assert greeting_for_all_friends(None) is None
assert greeting_for_all_friends([]) is None
assert greeting_for_all_friends(["Bilal"]) == ["Hello, Bilal!"]
