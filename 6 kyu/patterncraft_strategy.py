class Fly:
    @staticmethod
    def move(unit):
        unit.position += 10


class Walk:
    @staticmethod
    def move(unit):
        unit.position += 1


class Viking:
    def __init__(self):
        self.move_behavior = Walk()
        self.position = 0

    def move(self):
        self.move_behavior.move(self)


viking = Viking()
viking.move()
assert viking.position == 1
viking.move()
assert viking.position == 2

viking = Viking()
viking.move_behavior = Fly()
viking.move()
assert viking.position == 10
viking.move()
assert viking.position == 20

viking = Viking()
viking.move()
assert viking.position == 1
viking.move_behavior = Fly()
viking.move()
assert viking.position == 11
