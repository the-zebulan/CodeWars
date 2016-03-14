def process_2arrays(arr1, arr2):
    arr1 = set(arr1)
    arr2 = set(arr2)
    diff = len(arr1 - arr2)
    diff2 = len(arr2 - arr1)
    return [len(arr1 & arr2), diff + diff2, diff, diff2]
