class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self, n):
        if self.lives == 0:
            raise Exception('Omae wa mo shindeiru')
        elif n == self.number:
            return True
        self.lives -= 1
        return False


guesser = Guesser(10, 2)
guesser.guess(10)
guesser.guess(10)
guesser.guess(10)
guesser.guess(10)
assert guesser.guess(10) is True

guesser = Guesser(10, 2)
guesser.guess(1)
assert guesser.guess(1) is False
