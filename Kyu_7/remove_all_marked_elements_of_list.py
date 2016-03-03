class List(object):
    @staticmethod
    def remove_(integer_list, values_list):
        values_list = set(values_list)
        return filter(lambda a: a not in values_list, integer_list)
        # return [a for a in integer_list if a not in values_list]

l = List()
integers = [1, 1, 2, 3, 1, 2, 3, 4]
values = [1, 3]
assert l.remove_(integers, values) == [2, 2, 4]

integers = [1, 1, 2, 3, 1, 2, 3, 4, 4, 3, 5, 6, 7, 2, 8]
values = [1, 3, 4, 2]
assert l.remove_(integers, values) == [5, 6, 7, 8]

integers = [8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2, 3]
values = [2, 4, 3]
assert l.remove_(integers, values) == [8, 7, 6, 5, 1]
