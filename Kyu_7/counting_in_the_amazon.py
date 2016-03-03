def count_arara(num):
    adak, anane = divmod(num, 2)
    return ' '.join(['adak'] * adak + ['anane'] * anane)

assert count_arara(1) == "anane"
assert count_arara(2) == "adak"
assert count_arara(3) == "adak anane"
assert count_arara(9) == "adak adak adak adak anane"
