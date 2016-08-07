from collections import OrderedDict


def ordered_count(input_str):
    result = OrderedDict()
    for a in input_str:
        if a not in result:
            result[a] = 1
        else:
            result[a] += 1
    return result.items()
