PLAY = 'plays'
NOPE = 'does not play'


def areYouPlayingBanjo(name):
    """ are_you_playing_banjo == PEP8 (forced camelCase by codewars) """
    starts_with_r = name.startswith(('r', 'R'))
    return '{} {} banjo'.format(name, PLAY if starts_with_r else NOPE)

assert areYouPlayingBanjo('martin') == 'martin does not play banjo'
assert areYouPlayingBanjo('Rikke') == 'Rikke plays banjo'
