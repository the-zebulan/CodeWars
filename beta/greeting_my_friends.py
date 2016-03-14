GREET = 'Hello, {}!'.format


def greeting_for_all_friends(friends):
    return [GREET(a) for a in friends] if friends else None
