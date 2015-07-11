PLAY = 'plays'
NOPE = 'does not play'


def areYouPlayingBanjo(name):
    """ are_you_playing_banjo == PEP8 (forced camelCase by codewars) """
    return '{} {} banjo'.format(name, PLAY if name[0].lower() == 'r' else NOPE)

assert areYouPlayingBanjo('martin') == 'martin does not play banjo'
assert areYouPlayingBanjo('Rikke') == 'Rikke plays banjo'
