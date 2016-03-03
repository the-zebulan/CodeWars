def move(self, direction):
    x, y = map(int, self.position)
    if direction == 'up':
        x -= 1
    elif direction == 'down':
        x += 1
    elif direction == 'left':
        y -= 1
    elif direction == 'right':
        y += 1
    if 0 <= x <= 4 and 0 <= y <= 4:
        self.position = '{}{}'.format(x, y)
    else:
        raise IndexError('Error! Out of bounds!')

Hero.move = move
