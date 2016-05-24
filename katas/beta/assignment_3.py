# Python 2
from string import ascii_lowercase as az, maketrans


def keyword_cipher(s, keyword):
    seen = []
    letters = set(az)
    for a in keyword:
        if a not in seen:
            seen.append(a)
            letters.remove(a)
    seen.extend(sorted(letters))
    return s.lower().translate(maketrans(az, ''.join(seen)))


# # Python 3
# from string import ascii_lowercase as az
#
#
# def keyword_cipher(s, keyword):
#     cipher = []
#     letters = set(az)
#     for a in keyword:
#         if a not in cipher:
#             cipher.append(a)
#             letters.remove(a)
#     cipher.extend(sorted(letters))
#     return s.lower().translate(str.maketrans(az, ''.join(cipher)))
