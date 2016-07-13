def SubtractSum(n):
    """ subtract_sum == PEP8 (forced PascalCase by Codewars) """
    return 'apple'


# def SubtractSum(n):
#     """ subtract_sum == PEP8 (forced CamelCase by Codewars) """
#     fruits = [
#         'kiwi', 'pear', 'kiwi', 'banana', 'melon', 'banana', 'melon',
#         'pineapple', 'apple', 'pineapple', 'cucumber', 'pineapple',
#         'cucumber', 'orange', 'grape', 'orange', 'grape', 'apple', 'grape',
#         'cherry', 'pear', 'cherry', 'pear', 'kiwi', 'banana', 'kiwi',
#         'apple', 'melon', 'banana', 'melon', 'pineapple', 'melon',
#         'pineapple', 'cucumber', 'orange', 'apple', 'orange', 'grape',
#         'orange', 'grape', 'cherry', 'pear', 'cherry', 'pear', 'apple',
#         'pear', 'kiwi', 'banana', 'kiwi', 'banana', 'melon', 'pineapple',
#         'melon', 'apple', 'cucumber', 'pineapple', 'cucumber', 'orange',
#         'cucumber', 'orange', 'grape', 'cherry', 'apple', 'cherry', 'pear',
#         'cherry', 'pear', 'kiwi', 'pear', 'kiwi', 'banana', 'apple',
#         'banana', 'melon', 'pineapple', 'melon', 'pineapple', 'cucumber',
#         'pineapple', 'cucumber', 'apple', 'grape', 'orange', 'grape',
#         'cherry', 'grape', 'cherry', 'pear', 'cherry', 'apple', 'kiwi',
#         'banana', 'kiwi', 'banana', 'melon', 'banana', 'melon', 'pineapple',
#         'apple', 'pineapple'
#     ]
#     while True:
#         try:
#             n -= sum(int(a) for a in str(n))
#             return fruits[n - 1]
#         except IndexError:
#             pass
#
#
# print SubtractSum(325) == 'apple'
#
# # I tried making some more tests for myself and found out the answer
# # is always 'apple' so I changed my solution code
# from random import randint
#
# for _ in xrange(10):
#     n = randint(45, 1000)
#     print "SubtractSum({}), '{}'".format(n, SubtractSum(n))
