GREEK = {'alpha': 0, 'beta': 1, 'chi': 21, 'delta': 3, 'epsilon': 4, 'eta': 6,
         'gamma': 2, 'iota': 8, 'kappa': 9, 'lambda': 10, 'mu': 11, 'nu': 12,
         'omega': 23, 'omicron': 14, 'phi': 20, 'pi': 15, 'psi': 22, 'rho': 16,
         'sigma': 17, 'tau': 18, 'theta': 7, 'upsilon': 19, 'xi': 13, 'zeta': 5}


def greek_comparator(lhs, rhs):
    return ((-1, 1)[GREEK[lhs] > GREEK[rhs]], 0)[lhs == rhs]
    # return 0 if lhs == rhs else -1 if GREEK[lhs] < GREEK[rhs] else 1


assert greek_comparator('alpha', 'beta') == -1
assert greek_comparator('chi', 'chi') == 0
assert greek_comparator('upsilon', 'rho') == 1
