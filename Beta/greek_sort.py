greek_alphabet = ('alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta',
                  'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi',
                  'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi',
                  'chi', 'psi', 'omega')


def greek_comparator(lhs, rhs):
    return cmp(greek_alphabet.index(lhs), greek_alphabet.index(rhs))


assert greek_comparator('alpha', 'beta') == -1
assert greek_comparator('chi', 'chi') == 0
assert greek_comparator('upsilon', 'rho') == 1
