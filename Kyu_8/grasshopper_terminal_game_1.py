class Hero(object):
    def __init__(self, name='Hero'):
        self.damage = 5
        self.experience = 0
        self.health = 100
        self.name = name
        self.position = '00'

myHero = Hero()
assert myHero.name == 'Hero'
assert myHero.experience == 0
assert myHero.health == 100
assert myHero.position == '00'
assert myHero.damage == 5
