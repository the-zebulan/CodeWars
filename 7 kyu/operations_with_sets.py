def process_2arrays(arr1, arr2):
    arr1 = set(arr1)
    arr2 = set(arr2)
    diff = len(arr1 - arr2)
    diff2 = len(arr2 - arr1)
    return [len(arr1 & arr2), diff + diff2, diff, diff2]


arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr2 = [2, 4, 6, 8, 10, 12, 14]
assert process_2arrays(arr1, arr2) == [4, 8, 5, 3]

arr1 = [33, 2, 3, 37, 38, 40, 12, 10, 43, 44,
        47, 49, 8, 19, 22, 24, 26, 28, 29, 30]
arr2 = [1, 34, 17, 7, 9, 10, 43, 49, 22, 27, 28]
assert process_2arrays(arr1, arr2) == [5, 21, 15, 6]

arr1 = [32, 34, 3, 4, 39, 10, 43, 13, 11, 18, 21, 22, 7, 25, 26, 36]
arr2 = [32, 5, 38, 8, 41, 42, 12, 48, 40, 21, 22, 26, 10, 30]
assert process_2arrays(arr1, arr2) == [5, 20, 11, 9]

arr1 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25]
arr2 = [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]
assert process_2arrays(arr1, arr2) == [3, 19, 9, 10]
