# coding=utf-8
Position = {'high': 'h', 'low': 'l'}  # needed for hard coded tests


class Warrior(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.block = ''
        self.deceased = self.zombie = False

    @staticmethod
    def attack(enemy, position):
        damage = 0
        if enemy.block != position:
            damage += (5, 10)[position == 'h']
        if enemy.block == '':
            damage += 5
        enemy.set_health(enemy.health - damage)

    def set_health(self, new_health):
        if new_health == 0:
            self.deceased = True
            self.zombie = False
        elif self.deceased:
            self.zombie = True
        self.health = max(0, new_health)
