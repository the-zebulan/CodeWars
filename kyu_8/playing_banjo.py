PLAY = 'plays'
NOPE = 'does not play'


def areYouPlayingBanjo(name):
    """ are_you_playing_banjo == PEP8 (forced mixedCase by CodeWars) """
    return '{} {} banjo'.format(name, PLAY if name[0].lower() == 'r' else NOPE)
