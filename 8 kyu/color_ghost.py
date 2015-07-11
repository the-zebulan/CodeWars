from random import choice

COLORS = ('white', 'yellow', 'purple', 'red')


class Ghost(object):
    def __init__(self):
        self.color = choice(COLORS)

assert Ghost().color in COLORS
