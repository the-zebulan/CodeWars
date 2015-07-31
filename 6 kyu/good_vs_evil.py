G_WORTH = (1, 2, 3, 3, 4, 10)
E_WORTH = (1, 2, 2, 2, 3, 5, 10)
G_WIN = 'Good triumphs over Evil'
E_WIN = 'Evil eradicates all trace of Good'
TIE = 'No victor on this battle field'
OUTPUT = 'Battle Result: {}'.format


def goodVsEvil(good, evil):
    """ good_vs_evil == PEP8, forced camelCase by CodeWars """
    good = sum(int(a) * G_WORTH[i] for i, a in enumerate(good.split()))
    evil = sum(int(b) * E_WORTH[i] for i, b in enumerate(evil.split()))
    if good == evil:
        return OUTPUT(TIE)
    elif good > evil:
        return OUTPUT(G_WIN)
    return OUTPUT(E_WIN)

assert goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1') == 'Battle Result: Evil eradicates all trace of Good'
assert goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0') == 'Battle Result: Good triumphs over Evil'
assert goodVsEvil('1 0 0 0 0 0', '1 0 0 0 0 0 0') == 'Battle Result: No victor on this battle field'
