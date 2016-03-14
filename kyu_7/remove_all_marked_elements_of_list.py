class List(object):
    @staticmethod
    def remove_(integer_list, values_list):
        values_list = set(values_list)
        return filter(lambda a: a not in values_list, integer_list)
        # return [a for a in integer_list if a not in values_list]
