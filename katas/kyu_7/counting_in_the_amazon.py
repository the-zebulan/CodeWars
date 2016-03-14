def count_arara(num):
    adak, anane = divmod(num, 2)
    return ' '.join(['adak'] * adak + ['anane'] * anane)
