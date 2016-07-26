def square_it(digits):
    s = str(digits)
    s_len = len(s)
    len_sqrt = s_len ** 0.5
    int_sqrt = int(len_sqrt)
    if len_sqrt == int_sqrt:
        return '\n'.join(s[a:a + int_sqrt] for a in xrange(0, s_len, int_sqrt))
    return 'Not a perfect square!'
