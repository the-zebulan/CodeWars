from collections import Counter


def balance(arr1, arr2):
    return (sorted(Counter(arr1).itervalues()) ==
            sorted(Counter(arr2).itervalues()))
