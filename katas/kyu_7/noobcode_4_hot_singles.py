from collections import OrderedDict
from itertools import chain


def hot_singles(arr1, arr2):
    diff = set(arr1).symmetric_difference(arr2)
    return [a for a in OrderedDict.fromkeys(chain(arr1, arr2)) if a in diff]
