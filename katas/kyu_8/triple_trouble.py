def triple_trouble(one, two, three):
    return ''.join(''.join(a) for a in zip(one, two, three))
