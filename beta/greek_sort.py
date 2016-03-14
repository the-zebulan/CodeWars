greek_alphabet = ('alpha', 'beta', 'gamma', 'delta', 'epsilon', 'zeta', 'eta',
                  'theta', 'iota', 'kappa', 'lambda', 'mu', 'nu', 'xi',
                  'omicron', 'pi', 'rho', 'sigma', 'tau', 'upsilon', 'phi',
                  'chi', 'psi', 'omega')


def greek_comparator(lhs, rhs):
    return cmp(greek_alphabet.index(lhs), greek_alphabet.index(rhs))
