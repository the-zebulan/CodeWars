def how_much_i_love_you(nb_petals):
    return [
        'I love you',
        'a little',
        'a lot',
        'passionately',
        'madly',
        'not at all'
    ][(nb_petals % 6) - 1]
