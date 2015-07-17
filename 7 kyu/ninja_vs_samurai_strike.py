class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    @staticmethod
    def strike(enemy, swings):
        enemy.health = max((0, enemy.health - (swings * 10)))

ninja = Warrior('Ninja')
samurai = Warrior('Samurai')

samurai.strike(ninja, 3)
assert ninja.health == 70
