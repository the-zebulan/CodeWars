def evil(n):
    return 'It\'s {}!'.format(('Evil', 'Odious')[bin(n).count('1') % 2])
