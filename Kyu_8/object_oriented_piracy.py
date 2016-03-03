class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        return self.draft - self.crew * 1.5 > 20

Titanic = Ship(15, 10)
assert Titanic.is_worth_it() is False

Empty_Ship = Ship(0, 0)
assert Empty_Ship.is_worth_it() is False
