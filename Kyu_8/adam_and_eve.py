class Human:
    def __init__(self):
        pass


class Man(Human):
    pass


class Woman(Human):
    pass


def God():
    """ god == PEP8 (forced to capitalize by CodeWars) """
    return [Man(), Woman()]

paradise = God()
assert isinstance(paradise[0], Man) is True
