def greatest(x, y, n):
    for a in xrange(n - 1, max(x, y) - 1, -1):
        if not a % x and not a % y:
            return a
    return 0


def smallest(x, y, n):
    while True:
        n += 1
        if not n % x and not n % y:
            return n

# lcm / gcd ???

# print greatest(2, 3, 20)
# print greatest(5, 15, 100)
# print greatest(123, 456, 789)
#
# print smallest(2, 3, 20)
# print smallest(5, 15, 100)
# print smallest(123, 456, 789)

print greatest(1000000007, 1000000009, 10000000000000000000) == \
      9000000144000000567
print smallest(1000000007, 1000000009, 10000000000000000000) == \
      10000000160000000630
