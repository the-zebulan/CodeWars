hmm = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'


def base_64_to_base10(s):
    total = 0
    for i, a in enumerate(s[::-1]):
        print a, hmm.index(a) + (i * 64), '<<'
        total += hmm.index(a) + (i * 64)
    return total


print base_64_to_base10("/") # => 63
print base_64_to_base10("BA") # => 64
print base_64_to_base10("BB") # => 65
print base_64_to_base10("BC") # => 66
