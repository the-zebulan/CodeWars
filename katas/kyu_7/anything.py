class AlwaysTrue(object):
    __eq__ = __ne__ = __gt__ = __ge__ = __lt__ = __le__ = lambda _, __: True


def anything(*_):
    return AlwaysTrue()
