from collections import Counter


def scramble(s1, s2):
    # Minor refactor of a solution by 00kevin on CodeWars
    return not(Counter(s2) - Counter(s1))


# def scramble(s1, s2):
#     cnt = 0
#     length = len(s2)
#     s2 = sorted(s2)
#     for letter in sorted(s1):
#         if letter == s2[cnt]:
#             cnt += 1
#             if cnt == length:
#                 return True
#     return False
