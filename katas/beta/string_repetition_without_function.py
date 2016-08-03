# class str_repeat(object):
#     def __init__(self, strng, repetition):
#         self.repetition = repetition
#         self.strng = strng
#
#     def __eq__(self, other):
#         return self.strng * self.repetition == other


# solution by @suic on Codewars
str_repeat = str.__mul__
