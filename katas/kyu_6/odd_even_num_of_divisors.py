def oddity(n):
    return 'even' if n ** 0.5 % 1 else 'odd'


# def oddity(n):
#     result = 0
#     for a in xrange(1, int(n ** 0.5 + 1)):
#         if n % a == 0:
#             result += 1
#             if not a == n / a:
#                 result += 1
#     return 'odd' if result % 2 else 'even'
