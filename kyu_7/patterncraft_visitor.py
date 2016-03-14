class Thing(object):
    def __init__(self, health, damage):
        self.health = health
        self.damage = damage

    def accept(self, _):
        self.health -= self.damage


class Marine(Thing):
    def __init__(self):
        super(Marine, self).__init__(100, 21)


class Marauder(Thing):
    def __init__(self):
        super(Marauder, self).__init__(125, 32)


class TankBullet:
    pass
