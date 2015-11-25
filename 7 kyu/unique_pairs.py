from itertools import combinations


def projectPartners(n):
    """ project_partners == PEP8 (forced mixedCase by CodeWars) """
    return sum(1 for _ in combinations('0' * n, 2))


assert projectPartners(2) == 1
assert projectPartners(3) == 3
assert projectPartners(4) == 6
assert projectPartners(5) == 10
