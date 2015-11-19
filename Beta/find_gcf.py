from fractions import gcd as largestFactor  # largest_factor == PEP8

assert largestFactor(50, 25) == 25
assert largestFactor(81, 63) == 9
assert largestFactor(24, 54) == 6
assert largestFactor(67, 19) == 1
