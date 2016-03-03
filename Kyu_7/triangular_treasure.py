def triangular(n):
    return n * (n + 1) / 2 if n >= 0 else 0

assert triangular(0) == 0
assert triangular(2) == 3
assert triangular(3) == 6
assert triangular(-10) == 0
print triangular(613827063227449)
