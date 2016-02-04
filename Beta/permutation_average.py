from itertools import permutations


def permutation_average(n):
    perms_sum = total_perms = 0.0
    for a in permutations(str(n)):
        perms_sum += int(''.join(a))
        total_perms += 1
    return round(perms_sum / total_perms)


assert permutation_average(2) == 2
assert permutation_average(25) == 39
assert permutation_average(20) == 11
assert permutation_average(737) == 629
